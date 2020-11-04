#!/usr/bin/env python

"""
String formatting lab:

"""

# TASK one
# Write a format string that will take the values:
#     (2, 123.4567, 10000, 12345.67)
#     and produce:
#     'file_002 :   123.46, 1.00e+04, 1.23e+04'

print("file_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))
print()
# Note the subtle differnce between the 'e' and 'g' formatting strings.
#      I like 'g' -- it does significant figures.

# TASK one
# Same as above, a few slightly different ways:

# using the indices of the items:
print("file_{0:03d} : {1:10.2f}, "
      "{2:.2e}, {3:.3g}".format(2, 123.4567, 10000, 12345.67))
print()

# using named arguments:
print("file_{filenum:03d} : {two_digit:10.2f}, "
      "{exp:.2e}, {three_figs:.3g}".format(filenum=2,
                                           two_digit=123.4567,
                                           exp=10000,
                                           three_figs=12345.67))
print()

# and with an f-string:
filenum = 2
data = (123.4567, 10000, 12345.67)
print(f"file_{filenum:03d} : {data[0]:10.2f}, "
       "{data[1]:.2e}, {data[2]:.3g}")
print()


# Task Three
# Rewrite: "the 3 numbers are: %i, %i, %i"%(1,2,3)
#          for an arbitrary number of numbers...

# solution 1
# the goal was to demonstrate dynamic building of format strings:


def formatter(t):
    # The static part of the string
    fstring = "the {:d} numbers are: ".format(len(t))
    # This add the correct number of format specifiers:
    fstring += ", ".join(['{:d}'] * len(t))
    # The created string can be now applied to the tuple of numbers
    # * unpacks a sequence into the arguments of a function -- we'll get to that!
    return fstring.format(*t)


# call it with a couple different tuples of numbers:
print(formatter((2, 3, 5)))

print(formatter((2, 3, 5, 7, 9)))

# solution 2
# You may have realized that str() would make a nice string from
# a list or tuple
# perfectly OK to use that -- though it doesn't demonstrate how you can
# dynamically build up format strings, and then use them later...

numbers = (34, 12, 3, 56)

numbers_str = str(numbers)[1:-1]  # make a string, remove the brackets

# put it together with the rest of the string
print("the first {:d} numbers are: {}".format(len(numbers), numbers_str))


# Task Four
  # Given a 5 element tuple:

  #   ``( 4, 30, 2017, 2, 27)``

  #   use string formating to print:

  #   ``'02 27 2017 04 30'``

print("{3:02d} {4:02d} {2:4d} {0:02d} {1:02d}".format(4, 30, 2017, 2, 27))

# Task Five
# 
# Here's a task for you: Given the following four element list:
#     ``['oranges', 1.3, 'lemons', 1.1]``
# Write an f-string that will display:
#     ``The weight of an orange is 1.3 and the weight of a lemon is 1.1``

fruit = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {fruit[0][:-1]} is {fruit[1]} "
      f"and the weight of a {fruit[2][:-1]} is {fruit[3]}")

# Now see if you can change the f-string so that it displays
# the names of the fruit in upper case, and the weight 20% higher 
# that is 1.2 times higher).
print(f"The weight of an {fruit[0][:-1].upper()} is {1.2*fruit[1]} and "
      f"the weight of a {fruit[2][:-1].upper()} is {1.2*fruit[3]}")

# Task Six

data = [("Fred Barnes", 32, 32.12),
        ("Nancy Drew", 16, 1234.0),
        ("Wilt Chamberlain", 45, 20_000.0),
        ("Drew Barrymore", 52, 2.12),
        ]

for datum in data:
    print("{:25s} {:4d} ${:>10,.2f}".format(*datum))

# If you want to have the dollar sign line up with the number,
# that's trickier
print()
for datum in data:
    name = datum[0]
    age = datum[1]
    cost = "${:,.2f}".format(datum[2])
    print("{:25s} {:4d} {:>10s}".format(name, age, cost))

# Bonus extra:
# you can nest format specifiers to get a dynaic column width

# find the longest name:
print()
name_len = 0
for datum in data:
    name_len = max(name_len, len(datum[0]))

for datum in data:
    name = datum[0]
    age = datum[1]
    cost = "${:,.2f}".format(datum[2])
    print(f"{name:{name_len}s} {age:4d} {cost:>10s}")



# answer to bonus question at the very end:
# And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly 
# print the tuple in columns that are 5 charaters wide? It can be done on one short line!
the_tuple = tuple(range(10))
print()
print(('{:<5}'*len(the_tuple)).format(*the_tuple))
