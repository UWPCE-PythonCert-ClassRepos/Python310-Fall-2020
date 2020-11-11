
:orphan:

.. _notes_lesson05:

#####################################
11/19/2020: testing, testing, 1, 2, 3
#####################################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

| Hua Shao
|
| Vikram Raghavan
|
| Yazmery De Leon Guzman
|
| Matthew Edoimioya (Matt)


Issues that came up during the week.
====================================

A few of you have not gotten the first Mailroom submitted (and some missing earlier assignments as well).

Do remember that we need you to submit in Canvas -- with a link to a PR in the gitHub classroom repo, in order for us to know you've done it.



git and generated files
-----------------------

In general, you don't want to put generated files in git.

That could be files your code creates (next week anyway), or files ceated by your IDE, or Python itself (e.g. ``__pycache__``)

**Caution:** be very careful with ``git add .`` or ``git add *`` -- generally better to specifically add the files you now you need.

Or: ``git add *.py``

One "trick" is to run ``git status`` first, and you'll see what files are there that git will add ...


The ``.gitignore`` file
.......................

``.gitignore`` tells git what files you want it to ignore.
It is supposed to help keep you from accidentally adding extra stuff, and to keep git from bugging you about "untracked files" that you don't want it track.

We've put a ``.gitignore`` fiel in the classroom repos -- but gitHub is apparenlty sometimes skipping them :-(


Iterating through a Sequence
----------------------------

What's wrong with this code? 

(OK, not wrong, but less than ideal ....)

.. code-block:: python

    def list_donornames():
        """Lists all donors"""
        for i, __ in enumerate(list_donors):
            print(list_donors[i][0])

Code structure
--------------

That brings us to code structure:

This is a tricky topic -- hard to have clear "rules"

One thing to keep in mind is that any "block" of code (usually a function) should only have to know about what it is directly working with.

So a function that is doing something with a single donor should only know about a single donor -- it doesn't need to know about how all the donors are stored.

.. code-block:: python

    def total_donations(index):
        return sum(donor_table[index][1])

vs.

.. code-block:: python

    def total_donations(donor):
        return sum(donor[1])


Test names
----------

Try to give your tests meaningful names. If "test_3" fails, that doesn't tell you much, but if "test_donor_not_there" fails, you have a much better idea, at a glance, what may be wrong.

(Apologies: I put names like that in the ``test_walnut_party`` example)


``assert something is True`` ?
------------------------------

Is this necessary?

::

    assert something is True
    or
    assert something is False

Well, no. Assertions are, by definition, looking for Truthiness, so:

.. code-block:: python

    assert something
    or
    assert not something

will do just fine.

Long strings in code
--------------------

Sometimes you want to put a long string (too long for one line) in your code.
But using a triple-quoted string either puts in extra whitespace, or messes with the indentation of the code. 

Handy hint: two strings next to each other without anything (but whitespace) in between get joined by the python compiler:

.. code-block:: ipython

    In [10]: s = "part one:" "part two"

    In [11]: s
    Out[11]: 'part one:part two'

Combine that with an parentheses for implied line continuation:

.. code-block:: ipython

    In [15]: a_message = ("You can build up a long, "
        ...:              "string by putting it in "
        ...:              "multiple quoted lines.\n"
        ...:              "And even add newlines, and "
        ...:              "all sorts of other stuff!"
        ...:              )

    In [16]: print(a_message)
    You can build up a long, string by putting it in multiple quoted lines.
    And even add newlines, and all sorts of other stuff!

``sum``
-------

Did everyone find the ``sum()`` built in function?

How about ``max()`` and ``min()``


Mailroom with Exceptions and unit tests ...
-------------------------------------------

If you have a lot of names to import from a module:

.. code-block:: python

    from mailroom import (get_donor_index,
                          donor_list,
                          print_report,
                          donor_sort_by_total,
                          donor_sort_by_number_donations,
                         ...
                         )

But if I'm importing more than, say three or so names, I prefer to use a short name for the module:

.. code-block:: python

    import mailroom as mr

    mr.get_donor_index()


Testing printing...
-------------------

It really shouldn't be necessary to test printing -- Python's print function is well tested already :-) The trick is to make sure you don't have any logic that you do need to test in the code that's doing the printing.

And pytest is already "capturing" stdout, which is where print goes, so it's a bit tricky to do.

But if you REALLY need to do, this is how it can be done:

https://docs.pytest.org/en/stable/capture.html#accessing-captured-output-from-a-test-function

That makes use of a pytest "fixture" -- which we have not gotten into yet.

Let's check it out.


Lightning Talks
===============

Let's take a break and do some now.

| Hua Shao
|
| Vikram Raghavan


Review Mailroom?
================

Or move on to new material?


Time Check: I do want to have time to get to the new stuff!


If there is time:

Review Shadel's Code? or someone else's?



Packaging and Modules
=====================


https://uwpce-pythoncert.github.io/ProgrammingInPython/topics/10-modules_packages/index.html


Lightning Talks
===============

Let's take a break and do some now.

| Yazmery De Leon Guzman
|
| Matthew Edoimioya (Matt)


trigrams
--------

This is a really fun one -- but challenging.

Let's get a start on it!





New Assignments
===============


Exceptions
----------

Exceptions take a little while to "wrap your head around".

Shall we do the Exercise together?

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/except_exercise.html

