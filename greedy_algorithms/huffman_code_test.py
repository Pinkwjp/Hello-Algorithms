from typing import List
from string import ascii_lowercase
import random

from unittest import TestCase, main
from algorithms_refined.huffman_code import huffman_code

from huffman_code import huffman_binary_tree

letters = list(ascii_lowercase)


def unique_letters(num: int) -> List[str]:
    """return a list of num unique letters"""
    assert 0 < num <= len(letters)
    return random.sample(letters, num)


def unique_floats_sum_to_one(num: int) -> List[float]:
    """return a list of unique floats summing up to 1"""
    random_ints = random.sample(range(1, 100), k=num)
    total = sum(random_ints)
    return [(n / total) for n in random_ints]


class Huffman(TestCase):
    def test(self):
        for _ in range(100):
            num_max_24 = 12
            alphabets = unique_letters(num=num_max_24)
            frequencies = unique_floats_sum_to_one(num=num_max_24)
            tree = huffman_binary_tree(alphabets, frequencies)
            code_dict = huffman_code(tree)
            freq_dict = dict(zip(alphabets, frequencies))

            for a in code_dict:
                for b in code_dict:
                    freq_a = freq_dict[a]
                    freq_b = freq_dict[b]
                    code_a = code_dict[a]
                    code_b = code_dict[b]
                    with self.subTest(f'a: {a}, {freq_a}, {code_a}; b: {b}, {freq_b}, {code_b}'):
                        # higher frequency => shorter code
                        if freq_dict[a] >= freq_dict[b]:
                            self.assertTrue(len(code_a) <= len(code_b))
        

if __name__ == '__main__':
    main()