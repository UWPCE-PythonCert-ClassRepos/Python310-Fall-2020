"""
test code for the Report class(es)
"""

from report import Row, Report


def example_report():
    """
    utility function to provide a fresh report to test with
    """
    report = Report(limit=4)

    populate_report(report)
    return report


def populate_report(report):
    """
    utility function to populate an existing Report with
    some additional data

    :param report: the report object to populate

    The Report will be populated in place
    """
    report.add_row(Row("Natasha", "Smith", "WA"))
    report.add_row(Row("Devin", "Lei", "WA"))
    report.add_row(Row("Bob", "Li", "CA"))
    report.add_row(Row("Tracy", "Jones", "OR"))
    report.add_row(Row("Johnny", "Jakes", "WA"))
    report.add_row(Row("Derek", "Wright", "WA"))
    report.add_row(Row("Jordan", "Cooper", "WA"))
    report.add_row(Row("Mike", "Wong", "WA"))


# ###################
# tests for Row class
def test_row_init():
    """
    test that a new row has the proper attributes initialized
    """
    row1 = Row("Joe", "Camel", "WA")

    assert row1.fname == "Joe"
    assert row1.lname == "Camel"
    assert row1.state == "WA"


def test_row_id_unique():
    """ two Rows should have unique IDs """
    row1 = Row("Joe", "Camel", "WA")
    row2 = Row("Bob", "Camel", "WA")

    assert row1.id != row2.id


# ######################
# tests for Report class
def test_add_row():
    report = Report(4)

    report.add_row(Row("Fred", "Roberts", "MO"))

    # this is testing using and internal
    # implementation detail, which ou want to be careful of
    # but it will catch an error in the add_row, even when
    # the other methods are not yet written
    assert len(report.rows) == 1


def test_report_length():
    """
    test report size method
    """
    report = example_report()

    # the test data has 8 rows
    assert report.size() == 8


def test_number_of_pages():
    """
    check that the number of pages is correct
    """
    report = example_report()

    assert report.get_number_of_pages() == 2


def test_number_of_pages_after_change_limit():
    """
    check that the number of pages is correct
    """
    report = example_report()

    assert report.get_number_of_pages() == 2

    report.limit = 10

    assert report.get_number_of_pages() == 1


def test_number_of_pages_odd():
    """
    check that the number of pages is correct

    when there is an odd number
    """
    report = example_report()
    report.add_row(Row("Joe", "Camel", "WA"))

    assert report.get_number_of_pages() == 3


def test_find_row():
    """
    can a row be found by id?
    """
    report = example_report()

    row = report.rows[3]

    found = report.find_row(row.id)

    assert found.fname == row.fname
    assert found.id == row.id


def test_remove_rows():
    """
    test that you can remove a row by its ID
    """
    report = example_report()

    # get a row to test with
    row = report.rows[2]

    len_before = report.size()

    report.remove_row(row.id)

    assert report.size() == len_before - 1

    assert report.find_row(row.id) is None


def test_paged_rows_lname():
    report = example_report()

    rows = report.get_paged_rows("lname", 1)

    assert len(rows) == 4
    assert rows[0].lname == "Li"
    assert rows[-1].lname == "Wright"


def test_paged_rows_fname_reversed():
    report = example_report()

    rows = report.get_paged_rows("-fname", 0)

    assert len(rows) == 4
    assert rows[0].lname == "Jones"
    assert rows[-1].lname == "Cooper"


def test_paged_rows_state_odd():
    report = example_report()
    # add one more:
    report.add_row(Row("Joe", "Camel", "WA"))

    rows = report.get_paged_rows("state", 2)

    assert len(rows) == 1
    assert rows[0].lname == "Camel"


def test_paged_rows_state_odd_reverse():
    report = example_report()
    # add one more:
    report.add_row(Row("Joe", "Camel", "WA"))

    rows = report.get_paged_rows("-state", 2)

    assert len(rows) == 1
    assert rows[0].fname == "Bob"
    assert rows[0].lname == "Li"




