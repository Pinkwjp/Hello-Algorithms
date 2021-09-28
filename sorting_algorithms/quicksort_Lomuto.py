"""quicksort with Lomuto partition scheme"""

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


def quicksort(A: List[int], low, high) -> None:
    """sort a list of numbers"""
    if low < high:
        p = partition(A, low, high)
        quicksort(A, low, p-1)
        quicksort(A, p+1, high)


def test():
    for _ in range(1000):
        n = randint(2, 40)
        numbers = [randint(0, 1000) for _ in range(n)]
        result = sorted(list(numbers))
        quicksort(numbers, 0, len(numbers)-1)
        assert numbers == result


if __name__ == "__main__":
    test()
