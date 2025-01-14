from __future__ import annotations

import logging

from typing import Any

from mknodes.basenodes import mkimage


logger = logging.getLogger(__name__)


class MkBinaryImage(mkimage.MkImage):
    """Image carrying the data by itself.

    This node basically is a regular image link, but carries the image data by itself.
    The data will get written to the "virtual" folder at the end of the process.
    It can hold either str or bytes as data.
    """

    ICON = "material/file-image"

    def __init__(self, data: bytes | str, path: str, **kwargs: Any):
        """Constructor.

        Arguments:
            data: Image data
            path: path for the image (including extension)
            kwargs: Keyword arguments passed to parent
        """
        super().__init__(path=path, **kwargs)
        self.data = data

    def virtual_files(self):
        return {self.path: self.data}

    @staticmethod
    def create_example_page(page):
        import mknodes

        page += "A BinaryImage carries the image data by itself."
        page += "A file containing the data will become part of the file tree later on."
        data = """<svg width="90pt" height="90pt" version="1.1"
        viewBox="0 0 15.875 10.583" xmlns="http://www.w3.org/2000/svg">
         <g fill="none" stroke="#F00" stroke-width=".3">
          <path d="m6.1295 3.6601 3.2632 3.2632z"/>
          <path d="m9.3927 3.6601-3.2632 3.2632z"/>
         </g>
        </svg>
        """
        node = MkBinaryImage(data, path="some_image.svg", caption="A simple cross")
        page += mknodes.MkReprRawRendered(node)
