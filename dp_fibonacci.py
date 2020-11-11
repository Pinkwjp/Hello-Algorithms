
# mypy dp_fibonacci.py

memo = {1: 0, 2: 1}
def fibo(n: int) -> int:
    """
    n - positive inteter
    return the n-th fibonacci number
    """
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


def fibo_iter(n: int) -> int:
    """
    n - positive inteter
    return the n-th fibonacci number
    """
    memo = {1: 0, 2: 1}
    if n not in memo:
        i = 3
        while i <= n:
            memo[i] = memo[i-1] + memo[i-2]
            i += 1
    return memo[n]

