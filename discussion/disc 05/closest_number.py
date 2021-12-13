def closest_number(nums, target):
    """
    >>> closest_number([1, 4, 5, 6, 7], 2)
    1
    >>> closest_number([3, 1, 5, 6, 13], 4) #  choose the earlier number since there's a tie
    3
    >>> closest_number([34, 102, 8, 5, 23], 25)
    23
    """
    ans=nums[0]
    for i in nums:
        if abs(target-i)<abs(target-ans):
            ans=i
    return ans