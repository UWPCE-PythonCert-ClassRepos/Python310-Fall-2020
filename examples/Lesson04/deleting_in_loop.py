#!/usr/bin/env python

"""
What happens when you delete from a list while looping through it?
"""

a_list = list(range(10))
print("the original", a_list)
# loop to remove almost everything...

# for num in a_list[:]:
#     if num:  # is it an nonzero number?
#         a_list.remove(num)
#     print(a_list)
# print("after removing some", a_list)

# is that what you expected?


# what about adding stuff?
a_list = list(range(10))
new_list = []
for item in a_list:
    new_list.append(item)
    if item % 2:  # duplicate odd numbers
        new_list.append(item)
    print(new_list)

print("after adding odd numbers", new_list)

# #