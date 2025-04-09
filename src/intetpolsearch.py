def interpolation_search(arr, elem):
    if not arr:
        return []
    if elem < arr[0] or elem > arr[-1]:
        return None
    comparisons = []
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= elem <= arr[high]:
        if arr[low] == arr[high]:
            comparisons.append(arr[low])
            return comparisons if arr[low] == elem else comparisons

        pos = low + ((elem - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if pos < low or pos > high:
            break

        current = arr[pos]
        comparisons.append(current)

        if current == elem:
            return comparisons
        elif current < elem:
            low = pos + 1
        else:
            high = pos - 1

    return comparisons