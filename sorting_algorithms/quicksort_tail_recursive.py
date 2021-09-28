"""reducing the call stack of quicksort by using tail recursion"""


from random import randint
from typing import List


def partition(A: List[int], low, high) -> int:
    """divide the list of numbers into two partitions

    return the index of the pivot number

    choosing the rightmost element in the range as pivot 
    (Lomuto partition scheme)
    """
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1


def quicksort_tail_recursive(A: List[int], low: int, high: int) -> None:
    while low < high:
        # partition and sort left subarray
        p = partition(A, low, high)
        quicksort_tail_recursive(A, low, p-1)
        low = p + 1


def quicksort_tail_recursive_optimized(A: List[int], low: int, high: int) -> None:
    """an optimized version of quicksort_tail_recursive 
    
    the worst-case stack depth is theta(lg n)"""
    while low < high:
        p = partition(A, low, high)
        # sort the shorter subarray
        if p < (low+high) // 2:
            quicksort_tail_recursive(A, low, p-1)
            low = p + 1
        else:
            quicksort_tail_recursive(A, p+1, high)
            high = p - 1


def test():
    for _ in range(1000):
        n = randint(2, 40)
        numbers = [randint(0, 1000) for _ in range(n)]
        result = sorted(list(numbers))
        #quicksort_tail_recursive(numbers, 0, len(numbers)-1)
        quicksort_tail_recursive_optimized(numbers, 0, len(numbers)-1)
        assert numbers == result


if __name__ == "__main__":
    test()
