#!/usr/bin/env python3

"""
mailroom assignment
"""

donors = [("Fred Jones", [100, 200, 300]),
          ("Amy Shumer", [2000, 4000, 1000]),
          ]


def find_donor(name):
    """
    finds if a donor is in the donor db

    :param name: name of donor to find

    :returns: the donor tuple if found, or None if not
    """
    for donor in donors:
        if name.lower() == donor[0].lower():
            return donor
    return None


def thank_you():
    print("do the thank you thing now")

def make_report():
    print("put report here")

def main():
    print("Welcome to Mailroom!")
    answer = ""
    while  answer != "q":
        print("Please select from the following")
        print("Quit: 'q', \n"
              "Thank you: 't'\n"
              "Report: 'r'")
        answer = input(" => ")
        answer = answer.strip()
        answer = answer[0:1].lower()
        if answer == 't':
            thank_you()
        elif answer == 'r':
            make_report()




if __name__ == "__main__":
    # main()
    assert find_donor("Fred Jones") is not None
    assert find_donor("Bob Jones") is None
    assert find_donor("Fred jones") is not None
