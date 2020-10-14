#!/usr/bin/env python3
"""
make a randomized schedule for lightning talks

This version developed live during class: 10/13/2020
"""

import random

infile = open("students.txt")

lines = infile.readlines()

# the zeroth line is the header. It can be deleted here:
# del lines[0]

# or use the "slice notation" to strt looping 
# after the zeroth line
names = []
for line in lines[1:]:
    # split on the colons toget the name
    # strip any whitespace so as not to get blank lines.
    name = line.split(":")[0].strip()
    print(name)
    # only append if name is not the empty string
    if name:
        names.append(name)

# shuffle for random order
random.shuffle(names)
print(names)

# create 9 lists to store the names:
sessions = []
for __ in range(9):
    sessions.append([])

for i, name in enumerate(names):
    print(i, name)
    # the mod (remainder) operator figures
    # out what session to put the name in.
    sessions[i % 9].append(name) 

# Now to write the schedule out:

with open('lightning_schedule.txt', 'w') as outfile:
    for i, session in enumerate(sessions):
        # i + 2 so that it goes 2 -- 10
        outfile.write(f"\nSession # {i+2}\n")
        outfile.write("==============\n")
        for name in session:
            outfile.write(name + '\n')








