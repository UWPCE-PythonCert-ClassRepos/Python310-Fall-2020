"""
some experiments
"""

lst = [5, 6]


# print("global names:")
# print([name for name in globals().keys() if not name.startswith("__")])

# print("local names:")
# print([name for name in locals().keys() if not name.startswith("__")])

# print

def func(x, z=lst):
    """
    this adds z to a_global_name
    """
    print("lst is:", z)

    z.append(8)

    print(z)

func(4)

print(lst)

func(4, [2, 3 , 3])

print(lst)





