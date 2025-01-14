import shutil
from pathlib import Path

from .core import ContextDir, Step
from .dependencies import pip_dependency


class ResourcePackerStep(Step):
    encoding = 'utf-8'

    def __init__(self, source_dir: ContextDir = 'input_dir'):
        self.source_dir: ContextDir = source_dir

    def __call__(self, path: Path, output_paths: list[Path]):
        parent_dir = self.context[self.source_dir]
        input_paths = [
            (parent_dir / f)
            for filename in path.open()
            if (f := filename.strip()) and not f.startswith('#')
        ]
        data = '\n\n'.join(f.read_text(self.encoding) for f in input_paths)

        for o_path in output_paths:
            o_path.parent.mkdir(parents=True, exist_ok=True)
        output_paths[0].write_text(data, self.encoding)
        for o_path in output_paths[1:]:
            shutil.copy(output_paths[0], o_path)

        input_paths.insert(0, path)
        return input_paths, output_paths


class CSSMinifierStep(Step):
    encoding = 'utf-8'

    @classmethod
    def get_dependencies(cls):
        return {
            pip_dependency('lightningcss')
        }

    def __init__(self,
                 error_recovery: bool = False,
                 parser_flags: dict[str, bool] | None = None,
                 unused_symbols: set[str] | None = None,
                 browsers_list: list[str] | None = ['defaults'],
                 minify: bool = True):

        self.error_recovery = error_recovery
        self.parser_flags = parser_flags or {}
        self.unused_symbols = unused_symbols
        self.browsers_list = browsers_list
        self.minify = minify

    def __call__(self, path: Path, output_paths: list[Path]):
        import lightningcss
        data = lightningcss.process_stylesheet(
            path.read_text(self.encoding),
            filename=str(path),
            error_recovery=self.error_recovery,
            parser_flags=lightningcss.calc_parser_flags(**self.parser_flags),
            unused_symbols=self.unused_symbols,
            browsers_list=self.browsers_list,
            minify=self.minify
        )
        for o_path in output_paths:
            o_path.parent.mkdir(parents=True, exist_ok=True)
        output_paths[0].write_text(data, self.encoding)
        for o_path in output_paths[1:]:
            shutil.copy(output_paths[0], o_path)


class HTMLMinifierStep(Step):
    encoding = 'utf-8'
    minify_css = False
    minify_js = False

    @classmethod
    def get_dependencies(cls):
        return {
            (
                pip_dependency('minify-html-onepass', check_name='minify_html_onepass')
                | pip_dependency('minify-html', check_name='minify_html')
            ),
        }

    def __call__(self, path: Path, output_paths: list[Path]):
        params = {'minify_css': self.minify_css, 'minify_js': self.minify_js}
        try:
            from minify_html_onepass import minify
        except ImportError:
            from minify_html import minify
            params |= {
                'do_not_minify_doctype': True,
                'ensure_spec_compliant_unquoted_attribute_values': True,
                'keep_spaces_between_attributes': True,
            }
        data = minify(path.read_text(self.encoding), **params)
        for o_path in output_paths:
            o_path.parent.mkdir(parents=True, exist_ok=True)
        output_paths[0].write_text(data, self.encoding)
        for o_path in output_paths[1:]:
            shutil.copy(output_paths[0], o_path)
