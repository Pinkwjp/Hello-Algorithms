"""randomized quicksort based on Lomuto partition scheme"""

from random import randint, sample
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


def randomized_partition(A: List[int], low, high) -> int:
    """a randomized and more efficient partiion scheme"""
    i = randint(low, high)
    A[i], A[high] = A[high], A[i]
    return partition(A, low, high)


def randomized_median_of_three_partition(A: List[int], low, high) -> int:
    """choose the pivot as the median (middle element) of a set of 3 
    elements randomly selected from the subarray
    
    more efficient than the randomized partition
    """
    if high - low > 2:
        i, j, k = sample(range(low, high+1), 3)
        # make A[j] the median of three
        if A[i] > A[k]:
            A[i], A[k] = A[k], A[i]
        if A[j] > A[k]:
            A[j], A[k] = A[k], A[j]
        # put A[j] at high (will be the pivot for partition)
        A[j], A[high] = A[high], A[j]
    return partition(A, low, high)


def quicksort(A: List[int], low, high) -> None:
    """sort a list of numbers"""
    if low < high:
        #p = partition(A, low, high)
        #p = randomized_partition(A, low, high)
        p = randomized_median_of_three_partition(A, low, high)
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
