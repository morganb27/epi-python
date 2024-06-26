from test_framework import generic_test


def parity(x: int) -> int:
    count = 0
    while x:
        x &= x - 1
        count += 1
    return 0 if count % 2 == 0 else 1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
