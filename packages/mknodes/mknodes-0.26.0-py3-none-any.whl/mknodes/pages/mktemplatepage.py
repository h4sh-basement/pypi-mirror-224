from __future__ import annotations

import abc

from collections.abc import Sequence
import logging

from mknodes.pages import mkpage, processors


logger = logging.getLogger(__name__)


class MkTemplatePage(mkpage.MkPage, metaclass=abc.ABCMeta):
    """Abstact Page used for templates."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._build()

    @abc.abstractmethod
    def get_processors(self) -> Sequence[processors.PageProcessor]:
        raise NotImplementedError

    def _build(self):
        self.items = []
        for processor in self.get_processors():
            if processor.check_if_apply(self):
                processor.append_section(self)

    # def to_markdown(self) -> str:
    #     self._build()
    #     return super().to_markdown()
