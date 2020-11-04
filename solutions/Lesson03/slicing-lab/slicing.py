#!/usr/bin/env python3

"""
One solution...
"""


def exchange_first_last(seq):
    """with the first and last items exchanged"""
    return seq[-1:] + seq[1:-1] + seq[:1]

assert exchange_first_last('something') == 'gomethins'
assert exchange_first_last(tuple(range(10))) == (9, 1, 2, 3, 4, 5, 6, 7, 8, 0)


def every_other_removed(seq):
    """With every other item removed"""
    return seq[::2]


assert every_other_removed('a word') == 'awr'


def first4_last4_every_other_removed(seq):
    """With the first and last 4 items removed, and every other item in between"""
    return seq[4:-4:2]


a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print(first4_last4_every_other_removed(a_tuple))
assert first4_last4_every_other_removed(a_tuple) == (5, 7)


def seq_reversed(seq):
    """With the elements reversed (just with slicing)"""
    return seq[::-1]


print(seq_reversed('a string'))
assert seq_reversed([3, 6, 1, 8, 3, 7]) == [7, 3, 8, 1, 6, 3]


def last_third_first_third_mid_third(seq):
    """with the last third, then first third, then the middle third in the new order."""
    i = len(seq) // 3
    return seq[-i:] + seq[:i] + seq[i:-i]


assert last_third_first_third_mid_third(tuple(range(12))) == (8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7)




