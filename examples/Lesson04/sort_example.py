"""
This is a sorting example -- useful for the mailroom exercise
"""


def sort_key(donor):
    """A sort key function that sorts a list by the last name in the data structure"""
    # print("called on:", donor)
    name = donor[0]  # the name is the first item in the donor tuple
    last_name = name.split()[1]  # thelast name is the seconds item in the name string
    return last_name.upper()  # we want to make sure the last name is upper-cases.

def sort_by_donations(donor):
    return sum(donor[1])

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

print("Sorted the regular way")
print(sorted(donor_db, key=sort_by_donations, reverse=True))
print()


# # Let's see how it works:
# print("Sorted with the default")
# print(sorted(donor_db))
# print()

# print("Sorted the regular way")
# print(sorted(donor_db, key=sort_key))
# print()

# print("Reverse Sorted:")
# print(sorted(donor_db, key=sort_key, reverse=True))
# print()

