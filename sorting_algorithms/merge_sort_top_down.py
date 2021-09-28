"""classic top down merge sort with recursion"""

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


def merge_sort_top_down(A: List[int]) -> List[int]:
    """sort a list of numbers"""
    n = len(A)
    if n < 2: return A 
    middle = n // 2
    sorted_left_half = merge_sort_top_down(A[:middle])
    sorted_right_half = merge_sort_top_down(A[middle:])
    sorted_combined = merge(sorted_left_half, sorted_right_half)
    return sorted_combined


def test():
    for _ in range(1000):
        numbers = [randint(0, 1000) for _ in range(30)]
        result = merge_sort_top_down(list(numbers))
        assert result == sorted(numbers)


if __name__ == "__main__": test()
