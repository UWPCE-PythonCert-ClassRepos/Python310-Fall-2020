#!/usr/bin/env python
"""
mailroom assignment

This version uses a dict for the main db, and exception handling to
check input, and has been factored to be amenable to testing.
"""

import sys
import math

# handy utility to make pretty printing easier
from textwrap import dedent


class Donor:
    def __init__(self, name):
        self.name = name
        self._donations = []

    def add_donation(self, donation_amt):
        donation_amt = self.validate_donation(donation_amt)
        self._donations.append(donation_amt)

    def validate_donation(self, donation_amt):
        donation_amt = float(donation_amt)
        if not (0 <= donation_amt <= 1_000_000):
            raise ValueError("Donation amount must be greater than zero and less than a million")
        return donation_amt




def get_donor_db():
    """
    Return an in-memory representation of the donor database

    Each donor is represented by a tuple -- kind of like a record
      in a database table

    The full collection uses a dict with a "normalized" version of
    the donor's name as the key:
       - all lower case
       - spaces normalized
       - could do tother things in the future

    You could get a bit fancier by having each "record" be a dict, with
      "name" and "donations" as keys.

    This is in a function, so that it's easy to get a "fresh" copy
    """

    return {'william gates iii': ("William Gates III", [653772.32, 12.17]),
            'jeff bezos': ("Jeff Bezos", [877.33]),
            'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
            'mark zuckerberg': ("Mark Zuckerberg",
                                [1663.23, 4300.87, 10432.0]),
            }


def initialize_donor_db():
    global donor_db
    donor_db = get_donor_db()


def normalize_name(name):
    """
    normalize the name to use as a key in the donors dict
    """
    name = " ".join(name.strip().split()).lower()

    return name


def list_donors():
    """
    creates a list of the donors as a string, so they can be printed

    Not calling print from here makes it more flexible and easier to
    test
    """
    listing = ["\nDonor list:"]
    for donor in donor_db.values():
        listing.append(donor[0])
    return "\n".join(listing)


def find_donor(name):
    """
    find a donor in the donor db

    :param: the name of the donor

    :returns: The donor data structure -- None if not in the donor_db
    """
    return donor_db.get(normalize_name(name))


def add_donor(name):
    """
    Add a new donor to the donor db

    :param: the name of the donor

    :returns: the new Donor data structure
    """
    name = name.strip()
    donor = (name, [])
    donor_db[name.lower()] = donor
    return donor


def validate_donation(donation):
    """
    validates a dontation input for float,
    non-negative, etc.non-negative

    :param donation: the input donation
    :type donation: string

    :returns: float of donation amount

    raises a ValueError if invalid
    """

    donation = float(donation)

    # extra check here -- unlikely that someone will type "NaN", but
    # it IS possible, and it is a valid floating point number:
    # http://en.wikipedia.org/wiki/NaN
    if math.isnan(donation) or math.isinf(donation):
        raise ValueError

    if donation < 0:
        raise ValueError("donation can't be negative")

    if donation < 0.01:
        raise ValueError("donation can't be less than one cent")

    return donation


# def main_menu_selection():
#     """
#     Print out the main application menu and then read the user input.
#     """
#     action = input(dedent('''
#       Choose an action:

#       1 - Send a Thank You
#       2 - Create a Report
#       3 - Send letters to everyone
#       4 - Quit

#       > '''))
#     return action.strip()


def gen_letter(donor):
    """
    Generate a thank you letter for the donor

    :param: donor tuple

    :returns: string with letter

    note: This doesn't actually write to a file -- that's a separate
          function. This makes it more flexible and easier to test.
    """
    return dedent('''Dear {0:s},

          Thank you for your very kind donation of ${1:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1]))


def get_donation_amount():
    """ Get the donation amount"""
    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.
    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit) > ").strip()
        if amount_str == "menu":
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = validate_donation(amount_str)
        except ValueError:
            print("error: donation amount is invalid\n")
        else:
            break
    return amount


def get_donors_name():
    name = input("Enter a donors name (or 'menu' to exit) > ").strip()
    if name.lower() == "menu":
        return None
    else:
        return name


def print_donors_list():
    """
    print a list of existing donors
    """
    print(list_donors())
    return False


def add_donation(name, amount):
    """
    add a donation to the database
    """
    # If this is a new user, ensure that the database has the necessary
    # data structure.
    donor = find_donor(name)
    if donor is None:
        donor = add_donor(name)

    # Record the donation
    donor[1].append(amount)

    return donor


def send_thank_you():
    """
    Execute the logic to record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    name = get_donors_name()
    if name is None:
        return

    # Since this is also an exit point to the main menu,
    # we want to make sure this is done before mutating the db.
    amount = get_donation_amount()
    if amount is None:
        return

    # If it gets here, it should be a valid name and donation amount
    donor = add_donation(name, amount)
    print(gen_letter(donor))


def get_name(donor):
    # used to sort on name in donor_db
    return donor[1]


def generate_donor_report():
    """
    Generate the report of the donors and amounts donated.

    :returns: the donor report as a string.
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donor_db.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=get_name)
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"))
    report.append("-" * 66)
    for row in report_rows:
        report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
    return "\n".join(report)


def save_letters_to_disk():
    """
    make a letter for each donor, and save it to disk.
    """
    for donor in donor_db.values():
        letter = gen_letter(donor)
        # I don't like spaces in filenames...
        filename = donor[0].replace(" ", "_") + ".txt"
        print("writing: ", filename)
        open(filename, 'w').write(letter)


def print_donor_report():
    print(generate_donor_report())


