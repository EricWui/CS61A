def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if not branches(tree) and label(tree)==x:
        return [x]
    for branch in branches(tree):
        path = find_path(branch,x)
        if path and path[-1]==x:
            return [label(tree)]+path