"""
We have a set of requests {1, 2, . . . , n};  the ith request 
corresponds to an interval of time starting at s(i) and 
finishing at f (i). We’ll say that a subset of the requests 
is compatible if no two of them overlap in time. 

Our goal is to accept as large a compatible subset as possible. 
Compatible sets of maximum size will be called optimal.
"""

from typing import List
from collections import namedtuple

Request = namedtuple("Request", ["start", "finish"]) # (int, int)

def interval_scheduling(requests: List[Request]) -> List[Request]:
    """return a maximum list of compatible requests
    
    for any request i: 
    i.start >= 0, i.finish > i.start
    """
    selected: List[Request] = []
    sorted_requests = sorted(requests, key=lambda Request: Request.finish)
    previous_finish = -1  # ensure first one is selected
    for request in sorted_requests:
        if request.start > previous_finish:
            selected.append(request)
            previous_finish = request.finish
    return selected


def test():
    R_1 = [(2, 4),
           (3, 9),
           (5, 7),
           (1, 3)]
    requests_1 = [Request(*pair) for pair in R_1]
    assert interval_scheduling(requests_1) == [(1, 3), (5, 7)]


# mypy interval_scheduling.py 
if __name__ == "__main__": test()
