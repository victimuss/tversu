
def binSearch(A, elem):
    if not A:
        return []
    first = A[0]
    last = A[-1]
    if elem < first or elem > last:
        return None
    def helper(left, right):
        if left > right:
            return []
        mid = (left + right) // 2
        current = A[mid]
        if current == elem:
            return [current]
        elif elem < current:
            return [current] + helper(left, mid - 1)
        else:
            return [current] + helper(mid + 1, right)
    return helper(0, len(A) - 1)
print(" ".join((map(str,binSearch(A,elem)))))
