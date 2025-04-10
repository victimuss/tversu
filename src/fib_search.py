
def fibSearch(A, elem):

    if not A:
        return None
    if elem < A[0] or elem > A[-1]:
        return None
    n = len(A)

    f_prev, f_curr = 0, 1
    while f_curr < n:
        f_next = f_prev + f_curr
        f_prev, f_curr = f_curr, f_next


    comparisons = fibSearchRec(A, elem, 0, f_prev, f_curr, n)

    if not comparisons:
        return None
    return comparisons


def fibSearchRec(A, elem, lo, fKm1, fK, n):
    if fK <= 0 or fKm1 < 0:
        return []

    fKm2 = fK - fKm1
    mid = lo + fKm2 - 1
    if mid >= n:
        mid = n - 1
    if mid < lo:
        return []

    current = A[mid]
    comparisons = [current]

    if current == elem:
        return comparisons
    elif current < elem:
        new_lo = mid + 1
        right_comparisons = fibSearchRec(A, elem, new_lo, fKm2, fKm1, n)
        comparisons += right_comparisons
    else:
        new_fK = fKm2
        new_fKm1_val = fKm1 - fKm2
        left_comparisons = fibSearchRec(A, elem, lo, new_fKm1_val, new_fK, n)
        comparisons += left_comparisons

    return comparisons
