"""natural merge sort

quote:
"A natural merge sort is similar to a bottom-up merge sort 
except that any naturally occurring runs (sorted sequences) 
in the input are exploited. Both monotonic and bitonic (alternating up/down) 
runs may be exploited, with lists (or equivalently tapes or files) 
being convenient data structures (used as FIFO queues or LIFO stacks).
In the bottom-up merge sort, the starting point assumes each run 
is one item long. In practice, random input data will have many 
short runs that just happen to be sorted. In the typical case, 
the natural merge sort may not need as many passes because there 
are fewer runs to merge. In the best case, the input is already 
sorted (i.e., is one run), so the natural merge sort need only 
make one pass through the data. In many practical cases, 
long natural runs are present, and for that reason natural merge sort 
is exploited as the key component of Timsort. ..."

for more infor:
https://en.wikipedia.org/wiki/Merge_sort
"""


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


def merge_sort_natural(A: List[int]) -> List[int]:
    """sort a list of numbers"""
    if len(A) < 2: return A
    sorted_sublists: List[List[int]] = []
    # select naturally occurring sorted sublists
    sublist: List[int] = []
    for x in A:
        if (not sublist) or (sublist[-1] <= x):
            sublist.append(x)
        else:
            sorted_sublists.append(sublist)
            sublist = [x] 
    # collect the last sublist
    if sublist: sorted_sublists.append(sublist)
    # merge sublists
    while len(sorted_sublists) > 1:
        sublist_a = sorted_sublists.pop()
        sublist_b = sorted_sublists.pop()
        combined = merge(sublist_a, sublist_b)
        sorted_sublists.append(combined)
    return sorted_sublists.pop()


def test():
    for _ in range(1000):
        numbers = [randint(0, 1000) for _ in range(30)]
        result = merge_sort_natural(list(numbers))
        assert result == sorted(numbers)


if __name__ == "__main__":
    test()
