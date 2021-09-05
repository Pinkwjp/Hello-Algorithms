"""
The Weighted Interval Scheduling Problem is a strictly more general version 
of the Interval Scheduling Problem, in which each interval has a certain
value (or weight), and we want to accept a set of maximum value where no 
overlaping between any intervals of the selected set.
""" 

from collections import namedtuple
from typing import Dict, List, Optional

WeightedInterval = namedtuple('WeightedInterval', 
                              ['start', 'finish', 'value'])

def recur(intervals: List[WeightedInterval], 
          compatibles: Dict[int, Optional[int]],
          max_values: Dict[int, int], 
          i: int) -> int:
    """return the max value with compatible intervals from 0 to i"""
    if i in max_values:
        return max_values[i]
    # base case
    if i == 0:
        max_values[i] = intervals[0].value
    # non-base case, exclude or include current interval
    else:
        excluded = recur(intervals, compatibles, max_values, i-1)
        included = intervals[i].value
        j = compatibles[i]
        if j is not None: # j can be 0
            included += recur(intervals, compatibles, max_values, j)
        max_values[i] = max(included, excluded)
    return max_values[i]


def build_solution(intervals: List[WeightedInterval],
                   compatibles: Dict[int, Optional[int]],
                   max_values: Dict[int, int],
                   value_sum: int,
                   i: int) -> List[int]:
    """return a list of indexs from 0 to i that is included in a optimal solution"""
    j = compatibles[i]
    # base case, current interval is the last one to be inclueded
    if j is None:
        return [i]
    # excluede current interval
    if max_values[i-1] == value_sum:
        return build_solution(intervals, compatibles, max_values, value_sum, i-1)
    # include current interval
    else:
        value_sum -= intervals[i].value
        return build_solution(intervals, compatibles, max_values, value_sum, j) + [i]
    

def schedule(intervals: List[WeightedInterval]) -> List[WeightedInterval]:
    """return a list of compatible of intervals with the maximun value """
    # sorte intervals in increasing finish time
    sorted_intervals = sorted(intervals, key=lambda interval: interval.finish)
    # find maximun compatible interval for each interval
    compatibles: Dict[int, Optional[int]] = {}
    num = len(sorted_intervals)
    for i in range(num):
        # default value
        compatibles[i] = None
        # check all preceding intervals
        for j in range(i):
            if sorted_intervals[j].finish < sorted_intervals[i].start:
                compatibles[i] = j 
    # maximun value from interval 0 to interval i 
    max_values: Dict[int, int] = {}
    # recursive scheduling from the last interval
    recur(sorted_intervals, compatibles, max_values, num-1)
    # build solution using the optimal value
    max_sum = max_values[num-1]
    choosen = build_solution(sorted_intervals, compatibles, max_values, max_sum, num-1)
    return [sorted_intervals[i] for i in choosen]


def test():
    # (start, finish, value)
    tuples1 = [(2, 5, 2),
               (4, 8, 3),
               (7, 9, 7), 
               (3, 7, 4)]
    S1 = [WeightedInterval(*interval) for interval in tuples1]
    selected = schedule(S1)
    total_1 = 0
    for interval in selected:
        total_1 += interval.value
    assert total_1 == 9
    print()

    # (start, finish, value)
    tuples2 = [(1, 5, 3),
               (2, 7, 13),
               (6, 8, 8)]
    S2 = [WeightedInterval(*interval) for interval in tuples2]
    selected = schedule(S2)
    total_2 = 0
    for interval in selected:
        total_2 += interval.value
    assert total_2 == 13


# mypy weighted_interval_scheduling.py
if __name__ == "__main__":
    test()
