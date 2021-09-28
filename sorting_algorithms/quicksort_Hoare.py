"""quicksort with Hoare partition scheme"""

from random import randint
from typing import List


def partition(A: List[int], low, high) -> int:
    """divide the list of numbers into two partitions

    return the index of the pivot number
    
    Hoare partition scheme
    """
    pivot = A[(low+high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while A[i] < pivot: 
            i += 1
        j -= 1
        while A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else: 
            return j  


def quicksort(A: List[int], low, high) -> None:
    """sort a list of numbers"""
    if 0 <= low < high:
        p = partition(A, low, high)
        quicksort(A, low, p)
        quicksort(A, p+1, high)


def test():
    for _ in range(10):
        n = randint(2, 40)
        numbers = [randint(0, 1000) for _ in range(n)]
        result = sorted(list(numbers))
        quicksort(numbers, 0, len(numbers)-1)
        assert numbers == result


if __name__ == "__main__":
    test()
