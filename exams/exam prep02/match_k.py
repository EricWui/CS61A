def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def get_ans(num):
        apart_num=num%(10**k)
        while num>0:
            if apart_num!=(num%(10**k)):
                return False
            num//=(10**k)
        return True
    return get_ans


