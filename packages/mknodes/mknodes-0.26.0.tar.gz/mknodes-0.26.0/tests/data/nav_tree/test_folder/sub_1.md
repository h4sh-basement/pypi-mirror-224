````python exec="on"

import mknodes

path = mknodes.TEST_RESOURCES / "nav_tree/test_folder/markdown-exec.md"
node = mknodes.MkCode.for_file(path)
print(node)
node = mknodes.MkAdmonition("MkNodes also works great in combination with Markdown-exec!")
print(node)
````
