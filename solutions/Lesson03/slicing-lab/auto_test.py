#!/usr/bin/env python3

"""
some tests for the slicing lab

these should all pass if you run:

python auto_test.py
"""

import slicing


assert slicing.exchange_first_last('something') == 'gomethins'
assert slicing.exchange_first_last(list(range(10))) == [9, 1, 2, 3, 4, 5, 6, 7, 8, 0]
assert slicing.exchange_first_last(tuple(range(10))) == (9, 1, 2, 3, 4, 5, 6, 7, 8, 0)


assert slicing.every_other_removed('something') == 'smtig'
assert slicing.every_other_removed(list(range(10))) == [0, 2, 4, 6, 8]
assert slicing.every_other_removed(tuple(range(10))) == (0, 2, 4, 6, 8)


assert slicing.first4_last4_every_other_removed('firstandlast') == 'tn'
assert slicing.first4_last4_every_other_removed(list(range(10))) == [4]
assert slicing.first4_last4_every_other_removed(tuple(range(10))) == (4,)


assert slicing.seq_reversed('something') == 'gnihtemos'
assert slicing.seq_reversed(list(range(10))) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert slicing.seq_reversed(tuple(range(10))) == (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)


assert slicing.last_third_first_third_mid_third(tuple(range(1, 7))) == (5, 6, 1, 2, 3, 4)
assert slicing.last_third_first_third_mid_third(list(range(1, 7))) == [5, 6, 1, 2, 3, 4]
assert slicing.last_third_first_third_mid_third(list(range(1, 10))) == [7, 8, 9, 1, 2, 3, 4, 5, 6]



print("All Tests Passed")

