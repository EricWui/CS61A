def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if not branches(t):
        return label(t)
    return label(t)+max([max_path_sum(branch) for branch in branches(t)])
    