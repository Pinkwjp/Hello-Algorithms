"""
find out the greatest slice (summation) in a list of numbers
in linear time cost
"""

from typing import List, Tuple


def greatest_slice(numbers: List[int]) -> Tuple[int, int, int]:
    max_sum = -1 * sum([abs(n) for n in numbers])
    max_start = 0
    max_end = 0
    current_sum = 0
    start = 0
    for end, value in enumerate(numbers):
        current_sum += value
        if current_sum > max_sum:
            max_sum = current_sum
            max_end = end
            max_start = start
        if current_sum < 0:
            current_sum = 0
            start = end + 1 
    return max_sum, max_start, max_end
