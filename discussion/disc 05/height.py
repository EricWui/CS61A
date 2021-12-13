def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    "*** YOUR CODE HERE ***"
    if not branches(t):
        return 0
    return 1+max([height(branch) for branch in branches(t)])

