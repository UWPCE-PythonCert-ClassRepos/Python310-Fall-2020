#!/usr/bin/env python

"""
A set of classes to facilitate report writing
"""

import math
from operator import attrgetter
from uuid import uuid4


class Row:
    """
    This class represents a single row
    with ID, first name, last name and state attributes
    """

    def __init__(self, fname, lname, state):
        """
        initilzize a new row

        :param fname: The first name
        :param lname: The last name
        :param state: The two letter code of the state the person is from
        """
        self.id = str(uuid4())  # randomly generated unique ID
        self.fname = fname
        self.lname = lname
        self.state = state

    def __str__(self):
        return f"| {self.id} | {self.fname + ' ' + self.lname:<15} | {self.state} |"


class Report:
    def __init__(self, limit):
        """
        initilize a new report

        :param limit: the maximum number of rows in a page
        """
        self.limit = limit
        self._rows = []

    def add_row(self, row):
        """Add a row object to the report"""
        self._rows.append(row)

    def remove_row(self, row_id):
        """
        Remove a row object by the row's ID

        :param row_id: the id of the row to be removed
        """
        for r in self._rows:
            if r.id == row_id:
                break
        else:
            raise ValueError(f"No row with id: {row_id} in the report")
        self._rows.remove(r)

    def find_row(self, row_id):
        """
        find a Row by the row_id

        :param row_id: the id of the row you are looking for
        """
        for i, r in enumerate(self._rows):
            if r.id == row_id:
                return r
        return None

    def size(self):
        """
        Return how many total rows the report has
        """
        return len(self._rows)

    def get_number_of_pages(self):
        """
        Get how many pages the report has; this will be based on limit variable.
        If your limit=4 and rows list has 6 records then there are two pages:
          page1 has 4 records, page2 has 2 records
        hint: you'll want to round up
        """
        return math.ceil(self.size() / self.limit)

    def get_paged_rows(self, sort_field, page):
        """
        Return a list of rows for a specific page number
        :param sort_field:  field to sort on, e.g. "name" or "-name" (descending)
        :param page:        specific page for returning data
        :returns:           list of row objects for specific page

        Hints:
        1. You'll want to determine if sort is reversed or not (remember that
           sorted() takes in param for that) this is based on if the fields
           start with a minus sign for DESCENDING sort
        2. When sorting on passed in field you can use handy `operator` library
           with `attrgetter` method (look up official docs)
        3. To actually determine what rows belong on the specific page you'll be
           using list slicing (remember the slicing lab?)

           Here is an illustration to help with the code logic:

           The list has 6 rows => [<row1>, <row2>, <row3>, <row4>, <row5>, <row6>]
           for page=2 we expect to get => [<row5>, <row6>]
           with slicing you'll want to offset your list by 4 in this case
           (extra hint: we can define offset as `offset = (page - 1) * self.limit`)
        """
        sort_field = sort_field.strip()
        if sort_field.startswith("-"):
            reverse = True
            sort_field = sort_field.lstrip("-")
        else:
            reverse = False

        all_rows = sorted(self._rows, key=attrgetter(sort_field), reverse=reverse)

        for row in all_rows:
            print(row.fname, row.lname)
        return all_rows[page * self.limit: (page + 1) * self.limit]


def run_report(sort_field):
    print(f"... PAGED REPORT SORTED BY: '{sort_field}'...")
    page = 1
    while True:
        rows = report.get_paged_rows(sort_field, page=page)

        if not rows:
            break

        input(f"Press ENTER to see page {page}")

        print(f"PAGE: {page} of {report.get_number_of_pages()}")
        print("---------------------------------------------------------------")

        for row in rows:
            print(row)

        print("---------------------------------------------------------------")

        page += 1


if __name__ == "__main__":

    report = Report(4)

    report.add_row(Row("natasha", "smith", "WA"))
    report.add_row(Row("devin", "lei", "WA"))
    report.add_row(Row("bob", "li", "CA"))
    report.add_row(Row("tracy", "jones", "OR"))
    report.add_row(Row("johny", "jakes", "WA"))
    report.add_row(Row("derek", "wright", "WA"))

    run_report("fname")

    print("\n\nRemoving student: "
          f"{report.rows[1].fname} [{report.rows[1].row_id}]... \n\n")

    report.remove_row(report.rows[1].row_id)

    run_report("-fname")
