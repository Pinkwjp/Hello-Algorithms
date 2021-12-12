"""
find out the sum of the greatest slice in a list of numbers
using divide and conquer in loglinear cost.
(There is a linear time cost solution as well.)

TODO: use some bookkeeping to get start and end index of the greatest slice 
"""

from typing import List, Optional
from itertools import accumulate


def greatest_slice(numbers: List[int], i: int = 0, j: Optional[int] = None) -> int:
    """return the sum of a greatest slice of a list of number
    
    note: 
    the greatest slice will be the largest negative number 
    if all numbers are negative.
    """
    if j is None:
        j = len(numbers) - 1
    if i == j:
        return numbers[i]
    mid = (i + j) // 2
    return max(greatest_slice(numbers, i, mid), 
               crossing_middle(numbers, i, mid, j), 
               greatest_slice(numbers, mid+1, j))
    

def crossing_middle(numbers: List[int], start: int, mid: int, end: int):
    """return sum of the greatest slice crossing (containing) the number at mid"""
    assert start <= mid <= end
    left_slice_max_sum_with_middle = max(list(accumulate(reversed(numbers[start: mid+1]))))
    right_slice_max_sum_with_middle = max(list(accumulate(numbers[mid: end+1])))
    return (left_slice_max_sum_with_middle 
            + right_slice_max_sum_with_middle 
            - numbers[mid])
