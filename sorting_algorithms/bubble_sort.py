"""
implement the bubble sort and the optimized version

for more details, check out the wikipeida link:
https://en.wikipedia.org/wiki/Bubble_sort
"""

from random import randint
from typing import List


def bubble_sort_optimized(A: List[int]) -> List[int]:
    n = len(A)
    # need at most n-1 iterations
    for _ in range(n-1):
        new_n = 0
        for i in range(1, n):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
                new_n = i
        # all elements after the last swap are sorted,
        # and do not need to be checked again
        n = new_n
        if n <= 1:
            break
    return A


def bubble_sort_semi_optimized(A: List[int]) -> List[int]:
    n = len(A)
    swapped = False
    # need at most n-1 iterations
    for j in range(n-1):
        # the n-th pass finds the n-th largest element 
        # and puts it into its final place
        # so only need to check until the (n-1)st element
        for i in range(n-1-j):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True
        # no swap happened means the list is sorted already, done.
        if not swapped:
            break
    return A


def bubble_sort_basic(A: List[int]) -> List[int]:
    n = len(A)
    swapped = False
    # need at most n-1 iterations
    for _ in range(n-1):
        for i in range(n-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True
        # no swap happened means the list is sorted already, done.
        if not swapped:
            break
    return A 


def test():
    for _ in range(1000):
        numbers = [randint(0, 1000) for i in range(30)]
        sorted_numbers = sorted(numbers)
        A = list(numbers)
        B = list(numbers)
        C = list(numbers)
        a = bubble_sort_basic(A)
        b = bubble_sort_semi_optimized(B)
        c = bubble_sort_optimized(C)
        if not sorted_numbers == a == b == c:
            print(f'numbers: {numbers}')
            print(f'a: {a}')
            print(f'b: {b}')
            print(f'c: {c}')

# mypy bubble_sort.py 
# py bubble_sort.py
if __name__ == "__main__":
    test()
