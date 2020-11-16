"""
tests for mailroom
"""
import pytest

import mailroom as mr

def get_test_donors():

    return [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]


def test_find_donor_there():
    """
    check that it finds a donor that is there
    """
    # make sure to start with a clean test set
    mr.donor_db = get_test_donors()

    donor = mr.find_donor("Jeff Bezos")

    assert donor[0].lower() == "Jeff Bezos".lower()


def test_find_donor_not_there():
    """
    check that it finds a donor that is there
    """
    # make sure to start with a clean test set
    mr.donor_db = get_test_donors()
    donor = mr.find_donor("bob jones")

    assert donor is None


def test_donor_list():
    # make sure to start with a clean test set
    mr.donor_db = get_test_donors()

    listing = mr.donor_list()

    assert len(listing.split("\n")) == 4
    assert "Paul Allen" in listing
    assert "Jeff Bezos" in listing


def test_gen_letter():
    donor = ("Fred Flintstone", [100, 200, 300])
    letter = mr.gen_letter(donor)

    print(letter)

    assert letter.strip().startswith("Dear Fred Flintstone,")
    assert "$300.00" in letter


def test_make_donor_report():
    # make sure to start with a clean test set
    mr.donor_db = get_test_donors()

    report = mr.make_donor_report()

    print(report)

    assert len(report.split("\n")) == 6
    assert "Paul Allen" in report
    assert "Jeff Bezos" in report

    # a couple arbitray numbers:
    assert "16396.10" in report
    assert "326892.24" in report


def test_make_donor_report_sorted():
    # make sure to start with a clean test set
    mr.donor_db = get_test_donors()
    report = mr.make_donor_report()

    print(report)

    # make sure it's sorted properly
    totals = []
    for line in report.split("\n")[2:]:
        totals.append(float(line.split()[-3]))

    assert totals == sorted(totals)


def test_add_donor():
    """
    adds a new donor

    then tests that the donor is added, and that a donation is properly recorded.
    """
    # extra spaces should get stripped
    name = "Fred Flintstone  "

    donor = mr.add_donor(name)
    donor[1].append(300)
    assert donor[0] == "Fred Flintstone"
    assert donor[1] == [300]
    assert mr.find_donor(name) == donor


def test_add_donor_empty():
    # extra spaces should get stripped
    name = " "

    with pytest.raises(ValueError):
        donor = mr.add_donor(name)


def test_remove_donor_not_there():
    # make sure to start with a clean test set
    mr.donor_db = get_test_donors()

    result = mr.remove_donor("no one")

    assert result is False

def test_remove_donor_there():
    # make sure to start with a clean test set
    mr.donor_db = get_test_donors()

    result = mr.remove_donor("jeff bezos")

    assert result is True
    assert mr.find_donor("jeff bezon") is None


def test_convert_donation_value_integer():
    amount = mr.convert_donation_value("  12000")

    assert amount == 12000


def test_convert_donation_value_float():
    amount = mr.convert_donation_value("  12.50  ")

    assert amount == 12.5


def test_convert_donation_value_to_many_digits():
    amount = mr.convert_donation_value("  12.1234  ")

    assert amount == 12.12


def test_convert_donation_value_negative():
    with pytest.raises(ValueError):
        amount = mr.convert_donation_value("-12")


def test_convert_donation_value_non_number():
    with pytest.raises(ValueError):
        amount = mr.convert_donation_value("twelve")


def test_convert_donation_value_zero():
    with pytest.raises(ValueError):
        amount = mr.convert_donation_value("0")


def test_convert_donation_value_infinit():
    with pytest.raises(ValueError):
        amount = mr.convert_donation_value("Inf")
