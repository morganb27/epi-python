from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    for i in reversed(range(len(A))):
       if A[i] < 9:
           A[i] += 1
           return A
       A[i] = 0
    return [1] + A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
