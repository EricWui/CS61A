def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def prime(x):
        if x<=1:
            return True
        return False if n%x==0 else prime(x-1)
    return prime(n-1)

