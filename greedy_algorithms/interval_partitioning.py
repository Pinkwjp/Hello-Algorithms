"""
We have a set of requests {1, 2, . . . , n};  the ith request 
corresponds to an interval of time starting at s(i) and 
finishing at f (i).

we have many identical resources available and 
we wish to schedule all the requests using as few resources as possible. 
Because the goal here is to partition all intervals across multiple resources, 
we will refer to this as the Interval Partitioning Problem. 

The problem is also referred to as the Interval Coloring Problem.

We define the depth of a set of intervals to be the maximum number 
of intervals that pass over any single point on the time-line.
"""

from heapq import heappop, heappush
from itertools import repeat, count
from typing import Dict, List, Set, Tuple


from typing import List
from collections import namedtuple

Request = namedtuple("Request", ["start", "finish"])  # (int, int)


def interval_partitioning(requests: List[Request]) -> Dict[int, List[Request]]:
    """
    return the minimun partitioning of all the requests
    """
    requests.sort(key=lambda Request: Request.start)
    # labels[i] holds the label for requests[i]
    labels: List[int] = []  
    # numbers 0, 1, 2, ... as labels
    max_label = 0
    # attach label
    for j, current_request in enumerate(requests):
        usable_labels = set(range(max_label+1))
        # check all request starting before j
        for i in range(j):
            prev_request = requests[i]
            prev_label = labels[i]
            # check compatibility
            if prev_request.finish >= current_request.start:
                usable_labels.remove(prev_label)
        # attach label
        if usable_labels:
            label = usable_labels.pop() 
        else:
            max_label += 1
            label = max_label
        labels.append(label)
    # organize result
    groups: Dict[int, List[Request]] = {lab: [] for lab in range(max_label+1)}
    for i, lab in enumerate(labels):
        groups[lab].append(requests[i])
    return groups


def test():
    R_1 = [(1, 7),
           (3, 5),
           (4, 8),
           (9, 20)]
    requests_1 = [Request(*pair) for pair in R_1]
    groups = interval_partitioning(requests_1)
    from pprint import pprint
    pprint(groups)
    # {0: [Request(start=1, finish=7), Request(start=9, finish=20)],
    #  1: [Request(start=3, finish=5)],
    #  2: [Request(start=4, finish=8)]}


# mypy interval_partitioning.py
if __name__ == '__main__': 
    test()
