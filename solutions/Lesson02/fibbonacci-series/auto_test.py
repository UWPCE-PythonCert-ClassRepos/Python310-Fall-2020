from series import fibonacci, lucas, sum_series


assert fibonacci(-1) is None

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3

assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(2) == 3
assert lucas(3) == 4

assert sum_series(0) == fibonacci(0)
assert sum_series(1) == fibonacci(1)
assert sum_series(3) == fibonacci(3)

assert sum_series(0, 2, 1) == lucas(0)
assert sum_series(1, 2, 1) == lucas(1)
assert sum_series(3, 2, 1) == lucas(3)

assert sum_series(3, 3, 2) == 7
