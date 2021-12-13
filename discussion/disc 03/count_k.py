def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs 
    when taking up to and including k steps at a time. 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n==0 or n==1:
        return 1
    i=1
    sum=0
    while i<=k:
        if i>n:
            break
        sum+=count_k(n-i,k)
        i+=1
    return sum
    