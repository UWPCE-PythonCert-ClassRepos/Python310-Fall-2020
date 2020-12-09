#!/usr/bin/env python
"""
mailroom command line interface

"""

import sys
# handy utility to make pretty printing easier
from textwrap import dedent

from . import model as mr


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
            amount = mr.validate_donation(amount_str)
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
    print(mr.list_donors())
    return False


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
    donor = mr.add_donation(name, amount)
    print(mr.gen_letter(donor))


def print_donor_report():
    print(mr.generate_donor_report())


# Utilities for driving the menus:

def to_quit():
    sys.exit(0)


def return_to_menu():
    """ Return True to trigger exit out of sub-loop"""
    return True


def run_interactive_loop(action_dict, prompt_string):
    """
    this is the code to run an arbitrary interactive loop

    :param action_dict: dict mapping responses to actions

    :param prompt_string: text of the prompt.
    """
    while True:
        answer = input(prompt_string).strip()
        if answer:
            try:
                result = action_dict[answer]()
            except (KeyError):
                print(f'"{answer}" is not a valid input -- try again')
                continue
            if result:
                return

def thank_you_menu():

    selection_dict = {"1": send_thank_you,
                      "2": print_donors_list,
                      "3": return_to_menu,
                      }

    prompt = dedent('''
                  Choose an action:

                  1 - Process a Donation
                  2 - List Existing Donors
                  3 - Return to Main Menu
                  > ''')

    run_interactive_loop(selection_dict, prompt)


def main_menu():

    selection_dict = {"1": thank_you_menu,
                      "2": print_donor_report,
                      "3": mr.save_letters_to_disk,
                      "4": to_quit}

    prompt = dedent('''
                  Choose an action:

                  1 - Send a Thank You
                  2 - Create a Report
                  3 - Send letters to everyone
                  4 - Quit

                  > ''')

    run_interactive_loop(selection_dict, prompt)


def main():
    mr.initialize_donor_db()
    main_menu()


