
:orphan:

.. _notes_lesson06:

#############################
11/17/2020: Odd sentences ...
#############################


A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============


| Rose Nyameke
|
| Hua Shao
|
| Vikram Raghavan
|
| Farhan Samani
|
| Katrina Seok Taylor
|


Coding Workflow
===============

As you are developing your code, you *really* want to have an quick and efficient way to run you code and see if it's working, how it's changed, etc.

You may have noticed that for a program like Mailroom, you may have to do a few steps if user interaction to get to the part of the code you are working on. So how do you work on that efficiently?

The "right" way to do it is something called "Test Driven Development", which we are doing -- but hard for user-interaction!

* You want to break your code down into small functions that each do one thing.

* You should be able to run each function by itself.

If you are doing that, then as you develop your code, you can write and run each function until it's doing what it's supposed to do, and THEN put it all together.

One way to run a function is to call it in the ``__name__ == "__main__"`` block. You can then comment and uncomment each call as you work on your code.

So, for instance, while developing the interactive menues for mailroom:

.. code-block:: python

    if __name__ == "__main__":
        # create a global for the donor data.
        donor_db = get_donor_db()
        main_menu()
        # thank_you_menu

So I can uncomment our the menu code I'm working on.

Also: you really, really need a way to run your code with a couple keystrokes!!


Notes on Testing
================

Isolated tests
--------------

Each test should be isolated -- so that it doesn't rely on any other tests running first, or break any tests that come after it.

So how do you do that with test data that might change -- like a test for adding a new donor?

If you put some test data in a function:

.. code-block:: python

    def get_test_db():
        return {'william gates iii': ("William Gates III", [653772.32, 12.17]),
                'jeff bezos': ("Jeff Bezos", [877.33]),
                'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
                'mark zuckerberg': ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
                }

Then, in each test that needs a donor_db:

.. code-block:: python

    def test_something():
        # get a clean one to work with.
        db = get_test_db

This is a simple example of a "fixture". pytest has features to make more complex fixtures -- but this will do for now.

What if your donor db is global? YOu can reset that, too!

(Let's look at my solution)

Comprehensive Testing
---------------------

Comprehensive testing is HARD. In fact, it's impossible.

We do what we can -- but what to do when you find an issue that wasn't tested for?

In the supplied tests for trigrams, there was a test for make_sentence(): That's a tricky one, as it's supposed to be random. So it tested for some aspects of what the function returned, but very much missed some!

For example, one of you found:

"... ``make_sentence()`` function always returns 'Blind blind blind blind blind blind.' with test_dict"

Oops! that's clearly wrong. So what to do?

First -- maybe that wasn't very comprehensive test to begin with -- sorry.

But your tests will nver be comprehensive -- you will find bugs after the fact. So the when you do, the first thing to do is write a test that exercises that bug -- i.e. one that does fail with your broken code.


Minor issues that came up during the week.
==========================================


What does "in a dict" mean?
---------------------------

Remember that:

``something in a_dict`` checks if ``something`` is a key

So no need for:

``something in dict.keys()``


Looping through a dict
----------------------

If you need just the keys::

    for k in a_dict:
       ...

If you need just the values::

    for v in a_dict.values():
       ...

If you need both::

    for k, v in a_dict.items():
       ...


Getting an arbitrary key from a dict
------------------------------------

See ``arbitrary_key.py`` in `examples/lesson06`

Let's take a look ...



islice
------

This constuct is pretty cool for trigrams::

  for w1, w2, w3 in zip(word_list[:-2], word_list[1:-1], word_list[2:]):

But remember that slicing makes a copy -- so this is making three copies of the full word list. Computers have a LOT of memory these days, but it's still better to not waste it.

Turns out there is a alternative:

https://docs.python.org/3.7/library/itertools.html#itertools.islice

Lightning Talks
===============

Let's take a break and then hear some lightning talks:

|
| Rose Nyameke
|
| Hua Shao
|
| Vikram Raghavan
|


Mailroom issues:
================

dict as switch -- how do you leave the loop?
--------------------------------------------

Let's look at a particularly nifty solution:

``solutions/Lesson05/mailroom``


what does "global" mean?
------------------------

There is a "global" namespace, and there is the ``global`` keyword. What is the difference? when do you need to use ``global``?

TL;DR : There is nothing wrong with using global names -- but you VERY RARELY should use the ``global`` keyword!

(Devin's example)


``readlines()`` ?
-----------------

Quite a few of you have code like this:

.. code-block:: python

    with open(filename, "r") as f:
        full_lines = f.readlines()

    for line in full_lines:
        ...

Nothing wrong with that, but ...

``.readlines()``  reads the entire contents of the file into memory all at once.  Memory is big and cheap these days, but what if it's a REALLY big file?

If you are going to process the file line by line anyway, you might as well do:

.. code-block:: python

    with open(filename, "r") as f:
        for line in f:
            ...

That will loop though the file line by line, but only store one line at a time in memory.  The file system and disk should have a smart cache, so that it will be just as fast, but more memory efficient.

And one less line of code ...


Binary vs text files
--------------------

``open()`` uses text mode (default encoding -- utf-8?) by default. It will try to decode the file into text. If you open a binary file that way it will likely barf.

::

  open(the_filename, 'rb'

Is the way to open a binary file (note the "b") -- this weill read the bytes in the file, with no alteration.

For more on what "decode" means:

:ref:`unicode`

.. PythonCertDevel/modules/Unicode.html?highlight=unicode>`_


Any Questions about the homework -- or anything?
------------------------------------------------

review trigrams?

review mailroom?


Break and Lightning talks
=========================

|
| Farhan Samani
|
| Katrina Seok Taylor
|

New material:
=============

Comprehensions
--------------

Let's take a few minutes to go through it in class:

https://uwpce-pythoncert.github.io/ProgrammingInPython/exercises/comprehensions_lab.html


Advanced Argument Passing
-------------------------

All this ``*arg``, ``**kwargs`` stuff a bit confusing?

Let's explore it a bit.

AND -- we'll use TDD to do it.

Exercise in the class notes here:

https://uwpce-pythoncert.github.io/ProgrammingInPython/exercises/args_kwargs_lab.html


Modules and Packages
--------------------

Shall we take a look?

https://uwpce-pythoncert.github.io/ProgrammingInPython/exercises/packaging/package_lab.html








