from dp_fibonacci import *

# pytest dp_fibonacci_test.py 
# 10th fibonacci number - 34

def test_fibo():
    assert fibo(10) == 34

def test_fibo_iter():
    assert fibo_iter(10) == 34