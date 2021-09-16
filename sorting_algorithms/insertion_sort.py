"""
implement insertion sort 

for more details:
https://en.wikipedia.org/wiki/Insertion_sort
"""


from random import randint
from typing import List


def insertion_sort_optimized(A: List[int]) -> List[int]:
    """slightly optimized insertion sort
    
    compared to the basic version
    """
    for i in range(1, len(A)):
        x = A[i]
        j = i-1
        while j >= 0 and A[j] > x:
            # right shif but no swap
            # save 1 assignment 
            A[j+1] = A[j]
            j -= 1
        # value x is only assigned to a spot once 
        # instead of many time inside the while loop 
        A[j+1] = x 
    return A


def insertion_sort(A: List[int]) -> List[int]:
    """basic insertion sort"""
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
    return A 


def insertion_sort_recursive(A: List[int], n: int) -> None:
    if n == 0:
        return 
    else:
        insertion_sort_recursive(A, n-1)
        while n >= 1 and A[n-1] > A[n]:
            A[n-1], A[n] = A[n], A[n-1]
            n -= 1


def test():
    for _ in range(1000):
        numbers = [randint(0, 1000) for i in range(30)]
        sorted_numbers = sorted(numbers)
        A = list(numbers)
        B = list(numbers)
        C = list(numbers)
        a = insertion_sort(A)
        b = insertion_sort_optimized(B)
        insertion_sort_recursive(C, len(C)-1)
        c = C
        if not sorted_numbers == a == b == c:
            print(f'   {sorted_numbers}')
            print(f'a: {a}')
            print(f'b: {b}')
            print(f'c: {c}')


# mypy insertion_sort.py
# py insertion_sort.py
if __name__ == "__main__":
    test()

 