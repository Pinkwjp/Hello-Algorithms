from pprint import pprint
from dp_weighted_interval_scheduling import make_intervals
from dp_weighted_interval_scheduling import leftmost_compatible
from dp_weighted_interval_scheduling import main

# test_dp_weighted_interval_scheduling.py
# pytest test_dp_weighted_interval_scheduling.py -s

def test_make_intervals():
    for interval in make_intervals(5):
        print(interval)
    assert True

def test_leftmost_compatible():
    num = 5
    intervals = make_intervals(num)
    intervals.sort(key=lambda x: x.finish)
    pprint(intervals)
    L = leftmost_compatible(intervals)
    for i, compatible_index in enumerate(L):
        if compatible_index != None:
            j = compatible_index
            assert intervals[j].finish <= intervals[i].start

def test_main():
    for i in range(5):
        print(main())
        assert True
