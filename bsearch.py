def bsearch(lo, hi, predicate):
    while lo < hi:
        mid = lo + ((hi - lo) // 2)
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
