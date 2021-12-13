def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        t.label+= 0 if t.label%2==0 else 1
        return
    t.label+= 0 if t.label%2==0 else 1
    for branch in t.branches:
        make_even(branch)
