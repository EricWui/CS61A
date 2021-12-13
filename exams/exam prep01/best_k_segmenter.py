def best_k_segmenter(k, score):
    """
    >>> largest_digit_getter = best_k_segmenter(1, lambda x: x)
    >>> largest_digit_getter(12345)
    5
    >>> largest_digit_getter(245351)
    5
    >>> largest_pair_getter = best_k_segmenter(2, lambda x: x)
    >>> largest_pair_getter(12345)
    45
    >>> largest_pair_getter(245351)
    53
    >>> best_k_segmenter(1, lambda x: -x)(12345)
    1
    >>> best_k_segmenter(3, lambda x: (x // 10) % 10)(192837465)
    192
    """
    partitioner = lambda x: (x//(10**k), x%(10**k))
    def best_getter(n):
        assert n > 0
        best_seg = None
        while n>0:
            n, seg = partitioner(n)
            if best_seg==None or score(best_seg) < score(seg):
                best_seg = seg
        return best_seg
    return best_getter
