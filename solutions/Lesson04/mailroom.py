#!/usr/bin/env python3

"""
Mailroom Exercise -- with Exceptions -- and tested!
"""

from textwrap import dedent  # nifty utility!
import math

# In memory representation of the donor database
# using a tuple for each donor
# -- kind of like a record in a database table
# the donations are in a list -- so you can add to them
# Note the mutable inside an immutable

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

# loop through the donor list and get the names
def donor_list():
    names = []
    for donor in donor_db:
        names.append(donor[0])
    return "\n".join(names)

# loop through the donor list and get the names
def print_donors():
    print("Donor list:\n")
    print(donor_list())


def find_donor(name):
    """
    find a donor in the donor db

    :param: the name of the donor

    :returns: The donor data structure -- None if not in the donor_db
    """
    for donor in donor_db:
        # do a case-insenstive compare
        if name.strip().lower() == donor[0].lower():
            return donor
    return None


def add_donor(name):
    """
    add a new donor to the donor db
    """

    name = name.strip()
    if not name:
        raise ValueError("You must provide a name!")
    donor = (name, [])

    donor_db.append(donor)

    return donor


def remove_donor(name):
    """
    remove a donor from the donor db
    """
    name = name.strip()
    for idx, donor in enumerate(donor_db):
        # do a case-insenstive compare
        if name.lower() == donor[0].lower():
            del donor_db[idx]
            return True  # a donor was removed
    return False  # no donor removed


def main_menu_selection():
    """
    Print out the main application menu and then read the user input.
    """
    action = input(dedent('''
      Choose an action:

      't' - Send a Thank You
      'r' - Create a Report
      'q' - Quit

      > '''))
    return action.strip()


def gen_letter(donor):
    """
    Generate a thank you letter for the donor

    :param: donor tuple

    :returns: string with letter
    """
    return dedent('''
          Dear {},

          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.

                         Sincerely,
                            -The Team
          '''.format(donor[0], donor[1][-1]))


def convert_donation_value(response):
    """
    converts a string to a donation amount, and returns the value

    raises a ValueError if it can not be converted
    """
    errmsg = f"{response} is not a valid donation amount"
    try:
        amount = float(response)
    except ValueError:
        raise ValueError(errmsg)

    # round to cents.
    amount = round(amount, 2)
    if (math.isnan(amount) or  # this is getting a bit carried away...
        math.isinf(amount) or
        round(amount, 2) == 0.00 or
        amount < 0):
            raise ValueError(errmsg)
    return amount


def accept_donation(name):
    """
    prompt user for donor name and amount, and add it to the DB
    """
    while True:  # in case the name is not valid
        # get the donor from DB:
        donor = find_donor(name)
        # not already there
        if donor is None:
            try:
                donor = add_donor(name)
            except ValueError:
                print("you must supply a valid donor name")
                name = input("Provide the donor's name >")
                continue
        break

    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the donors list object.
    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit) > ").strip()
        if amount_str == "menu":
            # aborting -- removing donor record
            remove_donor(name)
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = convert_donation_value(amount_str)
        except ValueError:
            continue
        break

    # Record the donation
    # Note how the donor object can be manipulated while it is in the donors list.
    donor[1].append(amount)

    print(gen_letter(donor))


def send_thank_you():
    """
    Execute the logic to record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    while True:
        name = input("Enter a donor's name "
                     "(or 'list' to see all donors or 'menu' to exit)\n> ").strip()
        if name == "list":
            print_donors()
        elif name == "menu":
            break
        else:
            accept_donation(name)
            break
    return None


def sort_key(item):
    return item[1]


def make_donor_report():
    """
    Generate the report of the donors and amounts donated.
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donor_db:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=sort_key)
    # print it out in with a nice format.
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format(
                  "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    report.append("-" * 66)
    for row in report_rows:
        report.append("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

    return "\n".join(report)


def print_donor_report():
    """
    Generate the report of the donors and amounts donated.
    """
    print(make_donor_report())


if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu_selection()
        if selection == "t":
            send_thank_you()
        elif selection == "r":
            print_donor_report()
        elif selection == "q":
            running = False
        else:
            print("error: menu selection is invalid!")
