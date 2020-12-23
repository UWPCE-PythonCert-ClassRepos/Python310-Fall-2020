#!/usr/bin/env python
"""
This is an object oriented version
"""

import math
from textwrap import dedent
from operator import attrgetter


# Utility so we have data to test with, etc.
def get_sample_data():
    """
    returns a list of donor objects to use as sample data
    """
    return [Donor("William Gates III", [653772.32, 12.17]),
            Donor("Jeff Bezos", [877.33]),
            Donor("Paul Allen", [663.23, 43.87, 1.32]),
            Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]


class Donor():
    """
    class to hold the information about a single donor
    """

    def __init__(self, name, donations=None):
        """
        create a new Donor object

        :param name: the full name of the donor

        :param donations=None: iterable of past donations
        """

        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except TypeError:
                self.donations = [donations]

    @staticmethod
    def normalize_name(name):
        """
        return a normalized version of a name to use as a comparison key

        simple enough to not be in a method now, but maybe you'd want to make it fancier later.
        """
        return name.lower().strip().replace(" ", "")

    @property
    def last_donation(self):
        """
        The most recent donation made
        """
        try:
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donations / len(self.donations)

    @property
    def num_donations(self):
        return len(self.donations)

    def add_donation(self, amount):
        """
        add a new donation
        """
        amount = self.validate_donation(amount)
        self.donations.append(amount)

    @staticmethod
    def validate_donation(donation):
        """
        validates a donation input for float,
        non-negative, etc.

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


class DonorDB():
    """
    Encapsulation of the entire database of donors and data
    associated with them.
    """

    def __init__(self, donors=None):
        """
        Initialize a new donor database

        :param donors=None: iterable of Donor objects
        """
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}

    @property
    def donors(self):
        """
        An iterable of all the donors
        """
        return self.donor_data.values()

    def list_donors(self):
        """
        Creates a list of the donors as a string, so they can be printed

        Not calling print from here makes it more flexible and easier to
        test
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """
        find a donor in the donor db

        :param: the name of the donor

        :returns: The donor data structure -- None if not in the self.donor_data
        """
        return self.donor_data.get(Donor.normalize_name(name))

    def find_or_create_donor(self, name):
        """
        find a donor in the donor db

        if the donor is not already there,
        a new one is created and added to the db.

        :param: the name of the donor

        :returns: A Donor object -- empty if new
        """

        try:
            donor = self.donor_data[Donor.normalize_name(name)]
        except KeyError:
            donor = self.add_donor(name)
        # donor.add_donation(donation)
        return donor


    def add_donor(self, name):
        """
        Add a new donor to the donor db

        :param: the name of the donor

        :returns: the new Donor data structure
        """
        donor = Donor(name)
        self.donor_data[donor.norm_name] = donor
        return donor

    def gen_letter(self, donor):
        """
        Generate a thank you letter for the donor

        :param: Donor object

        :returns: string with letter

        note: This doesn't actually write to a file -- that's a separate
              function. This makes it more flexible and easier to test.
        """
        return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team
              '''.format(donor.name, donor.last_donation)
                      )

    @staticmethod
    def sort_key(item):
        # used to sort on name in self.donor_data
        return item[1]

    def generate_donor_report(self):
        """
        Generate the report of the donors and amounts donated.

        :returns: the donor report as a string.
        """
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)

        for donor in sorted(self.donor_data.values(),
                            key=attrgetter("total_donations")):
            report.append(f"{donor.name:25s}   "
                          f"${donor.total_donations:10.2f}   "
                          f"{donor.num_donations:9d}   "
                          f"${donor.average_donation:11.2f}")

        return "\n".join(report)

    def save_letters_to_disk(self):
        """
        make a letter for each donor, and save it to disk.
        """
        for donor in self.donor_data.values():
            print("Writing a letter to:", donor.name)
            letter = self.gen_letter(donor)
            # I don't like spaces in filenames...
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)
