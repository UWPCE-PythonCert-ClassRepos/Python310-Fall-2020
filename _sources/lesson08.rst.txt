
:orphan:

.. _notes_lesson08:

###########################
Dec 1, 2020: A Classy Topic
###########################


A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

David Brandt

Matt Parmett

Victor Alexander Orozco

Shadle A Stewart


Issues that came up during the week.
====================================


``for`` -- ``else``
-------------------

how many of you remember that you can use ``else`` with for?

From the Report Class:

.. code-block:: python

    def remove_row(self, row_id):

        """Remove a row object by the row ID"""

        for r in self.rows:
            if r.row_id == row_id:
                foundid = r
                break
        try:
            foundid == r
        except ValueError:
            print("Invalid row_id.")
        self.rows.remove(foundid)
        return None


What to test? And how?
----------------------

Make sure you test what matters about a function's result -- it's easiest (particularly if you wrote the code first) to simply match results, but your system will be more flexible if you test for the parts that matter, and won't change.

Ideally, your tests should be as isolated as possible. So if you, for instance, need to test that the correct letter is generated from a donor object, then create a donor object in the test, and pass that in, rather than pulling it from the donor_db -- that way, the donor_db could be broken, and the individual tests will pass.

For a function that creates substantial output -- like maybe a thanks you letter, yest parts of the letter that matter, rather than the entire text:

* Was the donor's name inserted correctly?

* Was the donation amount inserted correctly?

* any other part that tests the logic of the function.

That way, you can change the details of the letter template, and the tests will still pass.


Lightning Talks
---------------

Let's take a break and ...

David Brandt

Matt Parmett


The Report Class and basic OO
=============================


Any thoughts / questions?

did ``attrgetter`` make sense?



Lightning Talks
---------------

Victor Alexander Orozco

Shadle A Stewart


Magic Methods
=============

This next topic is key to making your classes "fit in" with the built-ins.

Let's start with the Row class -- and give it a __repr__: that would have helped a number of you with debugging :-)


Python static vs. class methods
-------------------------------

If any of you have a backgroun din Java/C++/C# -- this will be familiar, but maybe not what you expect.

So let's go over it a bit ...

:ref:`static_and_class_methods`


Circular Reasoning
------------------

Now let's get a start on the Circle class




