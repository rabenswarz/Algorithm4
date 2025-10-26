def interpolation_search(arr, lo, hi, x):
    if lo <= hi and arr[lo] <= x <= arr[hi]:
        pos = lo + ((hi-lo) * (x - arr[lo])) // (arr[hi] - arr[lo])
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation_search(arr, pos+1, hi, x)
        return interpolation_search(arr, lo, pos-1, x)
    return -1