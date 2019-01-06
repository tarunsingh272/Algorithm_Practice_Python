def search(self, root, val):
    """Search element in the BST with key"""
    p = root
    if p.value is None:  # empty tree
        return 0
    while p is not None and p.value != val:
        if val <= p.value:
            p = p.left
        else:
            p = p.right
    if p is not None:  # found the key
        return 1
    else:
        return 0