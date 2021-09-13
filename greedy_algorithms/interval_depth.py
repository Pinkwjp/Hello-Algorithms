"""
Determine the depth of a set of intervals.

We define the depth of a set of intervals to be the maximum number 
of intervals that pass over any single point on the time-line.

In the Interval Scheduling Problem, there is a single resource
and many requests in the form of time intervals, so we must choose which
requests to accept and which to reject. A related problem arises if we have
many identical resources available and we wish to schedule all the requests
using as few resources as possible. Because the goal here is to partition
all intervals across multiple resources, we will refer to this as the Interval
Partitioning Problem.

The minimun number of resources equal to the depth of the set of intervals
"""

from typing import List, Tuple
from collections import namedtuple

Request = namedtuple("Request", ["start", "finish"])  # (int, int)

def interval_depth(requests: List[Request]) -> int:
    """return the depth of a list of intervlas"""
    # a start add delta=1 to depth, a finish add delta=-1 to depth
    time_deltas: List[Tuple[int, int]] = [] 
    for start, finish in requests:
        time_deltas.append((start, 1))
        time_deltas.append((finish, -1))
    # sort in increasing time
    time_deltas.sort(key=lambda pair: pair[0])
    overall_depth = 0 
    current_depth = 0 
    # scan 
    for _, delta in time_deltas:
        current_depth += delta
        if current_depth > overall_depth:
            overall_depth = current_depth
    return overall_depth


def test():
    R_1 = [(3, 9),
           (5, 7),
           (1, 3)]
    requests_1 = [Request(*pair) for pair in R_1]
    assert interval_depth(requests_1) == 2

    R_2 = [(1, 2),
           (3, 4),
           (5, 6)]
    requests_2 = [Request(*pair) for pair in R_2]
    assert interval_depth(requests_2) == 1
    
    R_3 = [(1, 7),
           (3, 5),
           (4, 8),
           (9, 20)]
    requests_3 = [Request(*pair) for pair in R_3]
    assert interval_depth(requests_3) == 3

# mypy interval_depth.py
if __name__ == "__main__":
    test()
