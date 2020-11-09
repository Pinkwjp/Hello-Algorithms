from collections import namedtuple
from random import randint
from typing import Iterator
from pprint import pprint

# mypy dp_weighted_interval_scheduling.py

"""
dp_weighted_interval_scheduling.py

using dynamic programming to solve the weighted intervals scheduling problem
maximaize total weight (value) by chooseing a optimal compatible subset

variations:
- minimaize the weight (value) -> weighted interval scheduling (optimal minimal)
- set the weight (value) to 0 -> interval scheduling problem
"""

Interval = namedtuple('Interval', ['start','finish','weight'], defaults=[0,0,0])

def make_intervals(n: int) -> list:
    """
    return - a list of intervals sorted in non-decreasing-finish-time order
    """
    intervals = []
    for i in range(n):
        start = randint(1, 50)
        finish = start + randint(1, 20)
        value = randint(1, 10)
        intervals.append(Interval(start, finish, value))
    return sorted(intervals, key=lambda x: x.finish)

def leftmost_compatible(intervals: list) -> list:
    """
    intervals - sorted on non-decreasing finish time
    return - L, a list of compatible index

    L[i] = j
    - if j = None -> no compatible interval for i
    - else -> j is the leftmost compatible interval of i
    """
    L = []
    for i, interval in enumerate(intervals):
        j = None # if j = None -> no compatible interval for i
        for k in range(0, i): # all the left intervals to i
            left_interval = intervals[k]
            if left_interval.finish <= interval.start: # compatible
                j = k # keep updateing until the max j
        L.append(j) # index may be None, no compatible index
    return L

def weighted_intervals(intervals: list, P: list, W: dict, i: int) -> int:
    """
    intervals - sorted on non-decreasing finish time
    P - predecessor interval (leftmost compatible interval)
    W - optimal weight for intervals
    i - index for the current interval under consideration
    return - an optimal maximun value (int) of a compatible set of intervals
    """
    if i in W: return W[i]
    if i == 0: # the first interval
        W[i] = intervals[i].weight
    else:
        exclude_i = weighted_intervals(intervals, P, W, i-1) # excluding interval i
        include_i = intervals[i].weight # including interval i
        c = P[i] # the compatible interval of i
        if c != None:
            include_i += weighted_intervals(intervals, P, W, c) # include compatible
        W[i] = max(include_i, exclude_i)
    return W[i]

def build_solution(intervals: list, W: dict, P: list, max_index: int) -> Iterator[int]:
    max_weight = W[max_index] # the optimal maximun weight(value) that we found
    i = max_index # max index of all intervals
    while max_weight: # keep reducing to 0
        current = intervals[i].weight # current interval weight
        all_left_compatible = W.get(P[i], 0) # P[i] = can be none
        if current + all_left_compatible == max_weight: # part of the optimal solution
            yield i # yield solution indexs in decreasing order
            max_weight -= current
            i = P[i]
        else: # interval i is not part of the optimal solution
            i -= 1 # consider next one

def main():
    n = 5 # interval index:  0, 1, ... n-1
    W = dict()
    intervals = make_intervals(n)
    print('\n')
    pprint(intervals)
    P = leftmost_compatible(intervals) # predecessor interval (leftmost compatible)
    weighted_intervals(intervals, P, W, n-1)
    print('optimal maximun weight: ', W[n-1])
    solution_index_list = list(build_solution(intervals, W, P, n-1))
    solution_index_list.sort() # now indexs in increasing order
    return solution_index_list
