from typing import Dict, List, Optional, Tuple

Cache = Dict[Tuple[int, int], Optional[List[int]]]

def recur_lcs(results: Cache, A: List[int], i: int, B: List[int], j: int):
    """return the longest common sequence of A[:i] and B[:j]"""
    if (i, j) in results:
        return results[(i, j)]
    if i < 0 or j < 0: 
        result = []
    if A[i] == B[j]:
        result = recur_lcs(results, A, i-1, B, j-1)
        result.append(A[i])
    else:
        option_1 = recur_lcs(results, A, i-1, B, j)
        option_2 = recur_lcs(results, A, i, B, j-1)
        if len(option_1) > len(option_2): 
            result = option_1
        else:
            result = option_2
    results[(i, j)] = result
    return result


def longest_commom_sequence(A: List[int], B: List[int]):
    """
    return - one of the longest commom sequences between A, B
    """
    results: Cache = {}
    return recur_lcs(results, A, len(A)-1, B, len(B)-1)


def longest_commom_sequence_iterative(A: List[int], B: List[int]) -> List[int]:
    """
    return - one of the longest commom sequences between A, B
    """
    results: List[List[int]] = [[] * (len(B)+1)]
    for a in A:
        for j, b in enumerate(B, start=1):
            if a == b:
                results[j] = list(results[j-1])
                results[j].append(a)
            else:
                option_1 = results[j-1]
                option_2 = results[j]
                if len(option_1) > len(option_2):
                    results[j] = list(option_1)
                else:
                    results[j] = list(option_2)
    return results[-1]


def test():
    A = [1, 2, 3, 5, 8]
    B = [2, 3, 8]
    assert longest_commom_sequence(A, B) == B
    assert longest_commom_sequence_iterative(A, B) == B
    C = [1]
    D = [1]
    assert longest_commom_sequence(C, D) == [1]
    assert longest_commom_sequence_iterative(C, D) == [1]
    E = [2]
    F = [3]
    assert longest_commom_sequence(E, F) == []
    assert longest_commom_sequence_iterative(E, F) == []
