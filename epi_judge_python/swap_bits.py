from test_framework import generic_test


def swap_bits(x, i, j):
    bit_i = (x >> i) & 1
    bit_j = (x >> j) & 1
    print(x, i, j, bin(x))
    if bit_i != bit_j:
        mask = (1 << i) | (1 << j)
        x ^= mask

    return x
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
