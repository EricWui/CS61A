def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1==0 or n2==0:
        return n2 if n1==0 else n1
    n1_digit=n1%10
    n2_digit=n2%10
    num= (n2_digit*10)+n1_digit if n1_digit<n2_digit else (n1_digit*10)+n2_digit
    return num+merge(n1//10,n2//10)*100