from .mergelib import merge_sorted

# Implement merge_sort
# merge_sorted is a helper function that merges 2
# already sorted lists in linear time and space
# with respect to the combined lengths of the lists.

def merge_sort(data):
    """Return a new sorted list using merge sort (stable)."""
    n = len(data)
    if n <= 1:
        return data[:]  # или просто data, если ок вернуть тот же объект

    mid = n // 2
    left_sorted  = merge_sort(data[:mid])
    right_sorted = merge_sort(data[mid:])
    return merge_sorted(left_sorted, right_sorted)
