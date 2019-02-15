from binary_tree import TreeNode
"""仅抄了答案，需要重新研究"""


def top_down(root: TreeNode) -> TreeNode:
    p: TreeNode = root
    parent: TreeNode = None
    parent_right = None

    while p is not None:
        left: TreeNode = p.left
        p.left = parent_right
        parent_right = p.right
        p.right = parent
        parent = p
        p = left
    return parent


def dfs_bottom_up(p: TreeNode, parent: TreeNode) -> TreeNode:
    if p is None:
        return parent
    root = dfs_bottom_up(p.left, p)
    if parent is None:
        p.left = None
    else:
        p.left = parent.right
    p.right = parent
    return root


def bottom_up(root: TreeNode) -> TreeNode:
    return dfs_bottom_up(root, None)

