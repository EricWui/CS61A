# 不会写。。。
def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            checker = ____________________________
        i = ____________________________
    return ____________________________

def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            def outer(____________________________):
                def inner(____________________________):
                    return ____________________________
                return ____________________________
            checker = ____________________________
        i = ____________________________
    return ____________________________

