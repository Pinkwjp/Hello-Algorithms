"""
word game Fizz Buzz:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, 
Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz ... 

replace any number divisible by 3 with the word "Fizz"
replace any number divisible by 5 with the word "Buzz"
replace any number divisible by both 3 and 5 with the word "Fizz Buzz"
"""

from typing import List

def fizzbuzz(n: int) -> List[str]:
    # return a list of the frist n items (string) of fizzbuzz game
    assert isinstance(n, int) and n >= 1
    result = []
    # starting with '1'
    for i in range(1, n+1):
        divisible_by_3 = i % 3 == 0
        divisible_by_5 = i % 5 == 0
        val = ''
        if divisible_by_3:
            val = 'Fizz'
        if divisible_by_5:
            val = 'Buzz'
        if divisible_by_3 and divisible_by_5:
            val = 'Fizz Buzz'
        if not (divisible_by_3 or divisible_by_5):
            val = str(i)
        result.append(val)
        i += 1
    return result

assert fizzbuzz(1) == ['1']
assert ', '.join(fizzbuzz(10)) == '1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz'
assert ', '.join(fizzbuzz(15)) == '1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, \
11, Fizz, 13, 14, Fizz Buzz'

# mypy fizzbuzz.py
# py fizzbuzz.py