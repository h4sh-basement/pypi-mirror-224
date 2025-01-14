from __future__ import annotations

from pathlib import Path

from ..core import Step
from ..dependencies import pip_dependency


class AnchovyCSSStep(Step):
    """
    Simple Step to preprocess an Anchovy CSS file into compliant CSS.
    """
    encoding = 'utf-8'

    @classmethod
    def get_dependencies(cls):
        return {
            pip_dependency('tinycss2'),
        }

    def __call__(self, path: Path, output_paths: list[Path]):
        if not output_paths:
            return
        from .parser import process
        processed = process(path.read_text(self.encoding))
        for target_path in output_paths:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(processed, self.encoding)
