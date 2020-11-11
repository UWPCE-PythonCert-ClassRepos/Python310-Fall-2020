#!/usr/bin/env python

"""
test code for mailroom.py

"""

from mailroom import donor_db
from mailroom import check_if_in_list
from mailroom import get_name_index
from mailroom import get_sorted_donor_data
from mailroom import print_sorted_data_line
from mailroom import get_name_list
from mailroom import add_donor_if_needed
from mailroom import get_email_text


def test_check_if_in_list():
    assert check_if_in_list("Paul Allen", donor_db) is True
    assert check_if_in_list("Donald Trump", donor_db) is False


def test_get_name_index():
    assert get_name_index("Paul Allen", donor_db) == 2
    assert get_name_index("Donald Trump", donor_db) is None


def test_get_sorted_donor_data():
    test_data = get_sorted_donor_data(donor_db)
    assert test_data[0] == \
        ("William Gates, III", 653772.32 + 12.17, 2, (653772.32 + 12.17) / 2)


def test_print_sorted_data_line():
    assert print_sorted_data_line(
        ["William Gates, III", 653784.49, 2, 326892.24]) \
        == "William Gates, III         $  653784.49           2  $   326892.24"


def test_get_name_list():
    assert get_name_list(donor_db)[2] == "Paul Allen"


def test_add_donor_if_needed():
    donor_db_added = [("William Gates, III", [653772.32, 12.17]),
                      ("Jeff Bezos", [877.33]),
                      ("Paul Allen", [663.23, 43.87, 1.32]),
                      ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
                      ("Bill Boeing", []),
                      ]
    assert add_donor_if_needed("Bill Boeing", donor_db) == donor_db_added


def test_get_email_text():
    test_text = "Dear Joe Biden,\n" \
                "Thank you for your gracious donation of $100.00.\n" \
                "-The Mailroom"
    assert get_email_text("Joe Biden", 100.00) == test_text
