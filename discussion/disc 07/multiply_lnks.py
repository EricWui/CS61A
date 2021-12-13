def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    first = 1
    list_temp=[]
    if Link.empty in lst_of_lnks:
        return Link.empty
    for link in lst_of_lnks :
        first*=link.first
        link=link.rest
        list_temp+=[link]
    return Link(first, multiply_lnks(list_temp))
    
    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    

