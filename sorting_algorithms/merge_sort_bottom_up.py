"""iterative bottom up merge sort"""


from random import randint
from typing import List


def merge(A: List[int], B: List[int]) -> List[int]:
    """merge two sorted lists"""
    combined: List[int] = []
    while A and B:
        # merge backward, from big to small
        a = A.pop()
        b = B.pop()
        if a >= b:
            combined.append(a)
            B.append(b)
        else:
            combined.append(b)
            A.append(a)
    # either A or B is empty, put leftover in A
    A += B
    while A:
        combined.append(A.pop())
    # reverse to small to big
    combined.reverse()
    return combined


def merge_sort_bottom_up(A: List[int]) -> List[int]:
    """sort a list of numbers"""
    n = len(A)
    if n < 2: return A
    # sublist length 1, 2, 4, 8,..., n-1
    length = 1 
    while length < n-1:
        # merge all pairs of two sublist of size lenght
        for i in range(0, n, 2*length): 
            start = i
            middle = i+length
            end = min(i+2*length, n)
            sublist_1 = A[start:middle]
            sublist_2 = A[middle:end]
            combined_sorted = merge(sublist_1, sublist_2)
            # update corresponding part of original list
            A[start:end] = combined_sorted
        length *= 2
    return A 


def test():
    for _ in range(1000):
        numbers = [randint(0, 1000) for _ in range(30)]
        result = merge_sort_bottom_up(list(numbers))
        assert result == sorted(numbers)


if __name__ == "__main__":
    test()
