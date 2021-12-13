def is_palindrome(s):
    """
    >>> is_palindrome("tenet")
    True
    >>> is_palindrome("tenets")
    False
    >>> is_palindrome("raincar")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("ab")
    False
    """
    if len(s)<=1 or (len(s)==2 and s[0]==s[-1]):
        return True
    return False if s[0]!=s[-1] else is_palindrome(s[1:len(s)-1])