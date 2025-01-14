import typing

import mknodes

from mknodes.basenodes import mkadmonition


def create_index_page(nav: mknodes.MkNav):
    page = nav.add_page("Fancy index page", hide_toc=True, hide_nav=True)
    page += mknodes.MkShields(["version", "status", "codecov"])
    fn_code = mknodes.MkCode.for_object(create_index_page)
    node = mknodes.MkAdmonition(content=fn_code, title="")
    for i in typing.get_args(mkadmonition.AdmonitionTypeStr):
        node = mknodes.MkAdmonition(content=node, typ=i, title="")
    page += node
