"""
count the number of inversions within a sequence of number
"""

from random import randint
from typing import List, Optional, Tuple

def merge_and_count(left: List[int], right: List[int]) -> Tuple[List[int], int]:
    """
    merge sublists and count inversions
    
    left - left sorted sublist
    right - right sorted sublist

    return - combined sorted list and number of inversion
    """
    combined: List[int] = []
    inversion_count = 0
    i, j = 0, 0
    num_left, num_right = len(left), len(right)
    while i < num_left and j < num_right:
        a = left[i]
        b = right[j]
        if a <= b:
            combined.append(a)
            i += 1
        else:
            while a > b:
                combined.append(b)
                how_many_crossed_by_b = num_left - i
                inversion_count += how_many_crossed_by_b
                j += 1
                if j == num_right:
                    break
                b = right[j]
    combined += (left[i:] + right[j:])
    return combined, inversion_count


def count_inversion(A: List[int], 
                    low: int = 0, 
                    high: Optional[int] = None
                    ) -> Tuple[List[int], int]:
    """return the number of inversions in a list of integers"""
    if high is None:
        high = len(A) - 1
    if low == high:
        return [A[low]], 0
    else:
        middle = (low + high) // 2
        left_sublist_sorted, left_inversion_count = count_inversion(A, low, middle)
        right_sublist_sorted, right_inversion_count = count_inversion(A, middle+1, high)
        combined_list_sorted, cross_middle_inversion_count = merge_and_count(left=left_sublist_sorted, 
                                                                             right=right_sublist_sorted)
        combined_inversion_count = left_inversion_count + cross_middle_inversion_count + right_inversion_count
        return combined_list_sorted, combined_inversion_count


def count_inversion_brute_force(A: List[int]) -> int:
    result: int = 0
    for i, a in enumerate(A):
        for b in A[i+1:]:
            if a > b:
                result += 1
    return result 


def test():
    for _ in range(1000):
        numbers = [randint(0, 100) for i in range(8)]
        count_brute_force = count_inversion_brute_force(numbers)
        _, count = count_inversion(numbers)
        assert count_brute_force == count


# mypy count_inversion.py
if __name__ == '__main__': test()