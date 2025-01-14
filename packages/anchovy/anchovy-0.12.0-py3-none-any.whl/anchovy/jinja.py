from __future__ import annotations

import shutil
import sys
import typing as t
from functools import reduce
from pathlib import Path

from .core import Step
from .dependencies import pip_dependency, Dependency

if t.TYPE_CHECKING:
    from collections.abc import Sequence
    from jinja2 import Environment
    from markdown_it.renderer import RendererHTML
    from markdown_it.token import Token
    from markdown_it.utils import EnvType, OptionsDict

MDProcessor = t.Callable[[str], str]
MDContainerRenderer =  t.Callable[
    ['RendererHTML', 'Sequence[Token]', int, 'OptionsDict', 'EnvType'],
    str
]


class JinjaRenderStep(Step):
    """
    Abstract base class for Steps using Jinja rendering.
    """
    encoding = 'utf-8'

    @classmethod
    def get_dependencies(cls):
        return {
            pip_dependency('jinja2'),
        }

    def __init__(self,
                 env: Environment | None = None,
                 extra_globals: dict[str, t.Any] | None = None):
        if env and extra_globals:
            env.globals.update(extra_globals)
        self._env = env
        self._extra_globals = extra_globals

    @property
    def env(self):
        if self._env:
            return self._env

        from jinja2 import Environment, FileSystemLoader, select_autoescape
        self._env = Environment(
            loader=FileSystemLoader(self.context['input_dir']),
            autoescape=select_autoescape()
        )
        if self._extra_globals:
            self._env.globals.update(self._extra_globals)
        return self._env

    def render_template(self, template_name: str, meta: dict[str, t.Any], output_paths: list[Path]):
        """
        Look up a Jinja template by name and render it with @meta as
        parameters, then save the result to each of the provided @output_paths.
        """
        if not output_paths:
            return

        template = self.env.get_template(template_name)
        for path in output_paths:
            path.parent.mkdir(parents=True, exist_ok=True)
        template.stream(**meta).dump(str(output_paths[0]), encoding=self.encoding)
        for path in output_paths[1:]:
            shutil.copy(output_paths[0], path)

        return template.filename


class JinjaMarkdownStep(JinjaRenderStep):
    """
    A Step for rendering Markdown using Jinja templates. Parses according to
    CommonMark and Renders to HTML by default.
    """
    @classmethod
    def _build_markdownit(cls):
        import markdown_it
        processor = markdown_it.MarkdownIt()

        def convert(md_string: str) -> str:
            return processor.render(md_string)

        return convert

    @classmethod
    def _build_mistletoe(cls):
        import mistletoe
        processor = mistletoe.HTMLRenderer()

        def convert(md_string: str) -> str:
            return processor.render(mistletoe.Document(md_string))

        return convert

    @classmethod
    def _build_markdown(cls):
        import markdown
        processor = markdown.Markdown()

        def convert(md_string: str):
            return processor.convert(md_string)

        return convert

    @classmethod
    def _build_commonmark(cls):
        import commonmark
        parser = commonmark.Parser()
        renderer = commonmark.HtmlRenderer()

        def convert(md_string: str) -> str:
            return renderer.render(parser.parse(md_string))

        return convert

    @classmethod
    def get_options(cls):
        return [
            (pip_dependency('markdown-it-py', None, 'markdown_it'), cls._build_markdownit),
            (pip_dependency('mistletoe'), cls._build_mistletoe),
            (pip_dependency('markdown'), cls._build_markdown),
            (pip_dependency('commonmark'), cls._build_commonmark),
        ]

    @classmethod
    def get_dependencies(cls):
        deps = [option[0] for option in cls.get_options()]
        dep_set = {reduce(lambda x, y: x | y, deps)} if deps else set[Dependency]()

        return super().get_dependencies() | dep_set

    def __init__(self,
                 default_template: str | None = None,
                 md_processor: MDProcessor | None = None,
                 jinja_env: Environment | None = None,
                 jinja_globals: dict[str, t.Any] | None = None):
        super().__init__(jinja_env, jinja_globals)
        self.default_template = default_template
        self._md_processor = md_processor

    @property
    def md_processor(self):
        if not self._md_processor:
            for dep, factory in self.get_options():
                if dep.satisfied:
                    self._md_processor = factory()
                    break
            else:
                raise RuntimeError('Markdown processor could not be initialized!')
        return self._md_processor


    def __call__(self, path: Path, output_paths: list[Path]):
        meta, content = self.extract_metadata(path.read_text(self.encoding))
        meta |= {'rendered_markdown': self.md_processor(content.strip()).strip()}

        template_path = self.render_template(
            meta.get('template', self.default_template),
            meta,
            output_paths
        )
        if template_path:
            return [path, Path(template_path)], output_paths

    def extract_metadata(self, text: str):
        """
        Read metadata from the front of a markdown-formatted text.
        """
        meta = {}
        lines = text.splitlines()

        i = 0
        for line in lines:
            if ':' not in line:
                break
            key, value = line.split(':', 1)
            if not key.isidentifier():
                break

            meta[key.strip()] = value.strip()
            i += 1

        return meta, '\n'.join(lines[i:])


class JinjaExtendedMarkdownStep(JinjaRenderStep):
    encoding = 'utf-8'

    @classmethod
    def get_dependencies(cls):
        deps = super().get_dependencies() | {
            pip_dependency('markdown-it-py', check_name='markdown_it'),
            pip_dependency('mdit_py_plugins'),
            pip_dependency('Pygments', check_name='pygments'),
        }
        if sys.version_info < (3, 11):
            deps.add(pip_dependency('tomli'))
        return deps

    def __init__(self,
                 default_template: str | None = None,
                 jinja_env: Environment | None = None,
                 jinja_globals: dict[str, t.Any] | None = None,
                 *,
                 container_types: list[tuple[str | None, list[str]]] | None = None,
                 container_renderers: dict[str, MDContainerRenderer] | None = None,
                 substitutions: dict[str, str] | None = None,
                 auto_anchors: bool = False,
                 auto_typography: bool = True,
                 code_highlighting: bool = True,
                 pygments_params: dict[str, t.Any] | None = None,
                 wordcount: bool = False):
        super().__init__(jinja_env, jinja_globals)
        self.default_template = default_template
        self.container_types = container_types or []
        self.container_renderers = container_renderers or {}
        self.substitutions = substitutions or {}
        self.auto_anchors = auto_anchors
        self.auto_typography = auto_typography
        self.code_highlighting = code_highlighting
        self.pygments_params = pygments_params or {}
        self.wordcount = wordcount
        self._md_processor: t.Callable[[str], tuple[str, dict[str, t.Any]]] | None = None

    def __call__(self, path: Path, output_paths: list[Path]):
        md, meta = self.md_processor(
            self.apply_substitutions(
                path.read_text(self.encoding).strip()
            )
        )

        meta['rendered_markdown'] = md

        template_path = self.render_template(
            meta.get('template', self.default_template),
            meta,
            output_paths
        )
        if template_path:
            return [path, Path(template_path)], output_paths

    @property
    def md_processor(self):
        if not self._md_processor:
            self._md_processor = self._build_processor()
        return self._md_processor

    def apply_substitutions(self, text: str):
        for sub, value in self.substitutions.items():
            text = text.replace('${{ ' + sub + ' }}', value)
        return text

    def highlight_code(self, code: str, lang: str, lang_attrs: str):
        from pygments import highlight
        from pygments.formatters import HtmlFormatter
        from pygments.lexers import get_lexer_by_name, guess_lexer
        from pygments.util import ClassNotFound
        try:
            lexer = get_lexer_by_name(lang)
        except ClassNotFound:
            try:
                lexer = guess_lexer(code)
            except ClassNotFound:
                return ''

        return highlight(code, lexer, HtmlFormatter(**self.pygments_params))

    def _build_processor(self):
        import markdown_it
        # TODO Need for pyright suppression will be eliminated in the next
        # release of mdit_py_plugins:
        #  https://github.com/executablebooks/mdit-py-plugins/pull/91
        from mdit_py_plugins.anchors import anchors_plugin  # type: ignore[reportPrivateImportUsage]
        from mdit_py_plugins.attrs import attrs_block_plugin, attrs_plugin  # type: ignore[reportPrivateImportUsage]
        from mdit_py_plugins.container import container_plugin  # type: ignore[reportPrivateImportUsage]
        from mdit_py_plugins.front_matter import front_matter_plugin  # type: ignore[reportPrivateImportUsage]
        from mdit_py_plugins.wordcount import wordcount_plugin  # type: ignore[reportPrivateImportUsage]
        from .components import md_rendering

        processor = markdown_it.MarkdownIt(
            'commonmark',
            {
                'typographer': self.auto_typography,
                'highlight': self.highlight_code if self.code_highlighting else None,
            },
            renderer_cls=md_rendering.AnchovyRendererHTML
        )
        processor.enable(['strikethrough', 'table'])
        if self.auto_typography:
            processor.enable(['smartquotes', 'replacements'])
        if self.auto_anchors:
            anchors_plugin(processor)
        attrs_plugin(processor)
        attrs_block_plugin(processor)
        front_matter_plugin(processor)
        if self.wordcount:
            wordcount_plugin(processor)

        for tag, names in self.container_types:
            for name in names:
                renderer = (
                    self.container_renderers.get(name)
                    or (md_rendering.get_container_renderer(name, tag) if tag else None)
                )
                container_plugin(processor, name, render=renderer)

        def convert(md_string: str):
            env = {'anchovy_meta': dict[str, t.Any]()}
            md: str = processor.render(md_string, env=env)
            meta = env['anchovy_meta']
            if self.wordcount:
                meta['wordcount'] = env['wordcount']
            return md, meta

        return convert
