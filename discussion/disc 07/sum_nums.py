def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    if s==Link.empty:
        return 0
    return s.first+sum_nums(s.rest)
    

