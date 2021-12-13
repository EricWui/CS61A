def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """

    paths = []
    if t.is_leaf():
        return [[t.label]] if t.label==entry else [[]]
    for branch in t.branches:
        if find_paths(branch,entry)!=[[]]:
            paths+=[[t.label]+item for item in find_paths(branch,entry) if item[-1]==entry]
    return paths

