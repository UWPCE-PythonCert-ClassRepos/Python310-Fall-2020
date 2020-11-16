"""
tests for mailroom
"""

import mailroom as mr

def test_find_donor_there():
    """
    check that it finds a donor that is there
    """
    donor = mr.find_donor("Jeff Bezos")

    assert donor[0].lower() == "Jeff Bezos".lower()


def test_find_donor_not_there():
    """
    check that it finds a donor that is there
    """
    donor = mr.find_donor("bob jones")

    assert donor is None



