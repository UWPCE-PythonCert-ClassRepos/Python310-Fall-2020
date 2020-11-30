"""
Solutions to the comprehensions lab

Note that the first half of the lab you can run teh code
and see the answer for yourself.

But here are a few from the seconds part of the lab.
"""

# Count Evens:
# Using a list comprehension, return the number of evens
# integers in the given list.


def count_evens(nums):
    return len([x for x in nums if not x % 2])

assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0


# 1) Print the dict by passing it to a string format method,
#    so that you get something like:

#    “Chris is from Seattle, and he likes chocolate cake, mango fruit,
#     greek salad, and lasagna pasta”


# From the dicts/sets lab:
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

print("{name} is from {city}, and they like {cake} cake, "
      "{fruit} fruit {salad} salad and {pasta} pasta.".format(**food_prefs))


# 2) Using a list comprehension, build a dictionary of numbers from
#    zero to fifteen and the hexadecimal equivalent (string is fine).

#    (the hex() function gives you the hexidecimal representation of a
#    number as a string)

d = dict((i, hex(i)) for i in range(16))

print(d)


# 3) as a dict comp:

d = {i: hex(i) for i in range(16)}

print(d)

# 4) Using the dictionary from item (1): Make a dictionary using the
#    same keys but with the number of ‘a’s in each value. You can do
#    this either by editing the dict in place, or making a new one.
#    If you edit in place make a copy first!

num_As = {key: val.lower().count('a') for key, val in food_prefs.items()}

print(num_As)

# 5) Create sets s2, s3 and s4 that contain numbers from zero through
#    twenty, divisible 2, 3 and 4.

#    Do this with one set comprehension for each set.

s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}

print(s2)
print(s3)
print(s4)

# What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).

# Create a sequence that holds all the divisors you might want – could be 2,3,4, or could be any other arbitrary divisors.
# Loop through that sequence to build the sets up – so no repeated code. you will end up with a list of sets – one set for each divisor in your sequence.
# The idea here is that when you see three (Or more!) lines of code that are almost identical, then you you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.

divisors = (2, 3, 4, 5, 6)

multiples = {}
for div in divisors:
    multiples[div] = {i for i in range(21) if not i % div}


for div, mult in multiples.items():
    print(f"these numbers: {mult} are divisible by {div}")

# Extra credit: do it all as a one-liner by nesting a set comprehension
# inside a list comprehension. (OK, that may be getting carried away!)

multiples = {div: {i for i in range(21) if not i % div} for div in divisors}

print("All one nested comprehension:")
for div, mult in multiples.items():
    print(f"these numbers: {mult} are divisible by {div}")

