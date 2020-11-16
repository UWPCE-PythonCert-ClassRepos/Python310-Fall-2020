
:orphan:

.. _notes_lesson06:

##############################
11/17/2020: Odd senstences ...
##############################


A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

From last week:


| Hua Shao
|
| Vikram Raghavan
|
| Farhan Samani
|
| Katrina Seok Taylor
|
| Rose Nyameke


Comprehensions
--------------


Let's take a few minutes to go through it in class:

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/comprehensions_lab.html

Comprehensive Testing
=====================

Comprehensive testing is HARD. IN fact, it's impossible.

We do what we can -- but what to do when you find a hole?

In the supplied tests for trigrams, there was a test for make_sentence(): That's a tricky one, as it's supposed to be random. So it tested for some aspects of what the function returned, but very much missed some!

For example, one of you found:

"... ``make_sentence()`` function always returns 'Blind blind blind blind blind blind.' with test_dict"

Oops! that's clearly wrong. So what to do?

First -- maybe that wasn't very comprehensive test to begin with -- sorry.

But your tests will nver be comprehensive -- you will find bugs after teh fact. So the when you do, the first thing to do is write a test that exercises that bug -- i.e. one that does fail with your broken code.




Issues that came up during the week.
====================================

Minor Issues
------------

Remember that:

``something in a_dict`` checks if ``something`` is a key

similarly:

``for k in dict:``

loops through the keys. So no need for:

``for k in dict.keys():``



Getting an arbitrary key from a dict
------------------------------------

See ``arbitrary_key.py`` in `examples/lesson06`


nifty formatting
----------------

what the heck is this?

.. code-block:: python

    def data_print(info, widths):
        """
        takes in donor information and widths and returns a string formatted for
        printing for a donor report.
        """
        output_string = ""
        output_string += '{:<{width0}} ${:>{width1}.2f} {:^{width2}} ${:>{width3}}'.format(info[0], info[1], info[2], info[3], width0=widths[0], width1=widths[1]-1, width2=widths[2], width3=widths[3]-1)

cleaned up a bit::

    '{:<{widths[0]}} ${:>{widths[1]}.2f}'.format( "fred", 100, widths=widths)

islice
------

This constuct is pretty cool for trigrams::

  for w1, w2, w3 in zip(word_list[:-2], word_list[1:-1], word_list[2:]):

But remember that slicing makes a copy -- so this is making three copies of the full word list. Computers have a LOT of memory these days, but it's still better to not waste it.

Turns out there is a alternative:

https://docs.python.org/3.7/library/itertools.html#itertools.islice


Coding Workflow
---------------

As you are developing your code, you *really* want to have an quick and efficient way to run you code and see if it's working, how it's changed, etc.

You may have noticed that for a program like Mailroom, you may have to do a few steps if user interaction to get to the part of the code you are working on. So how do you work on that efficiently?

The "right" way to do it is something called "Test Driven Development", which we will get to soon. But in the meantime:

* You want to break your code down into small functions that each do one thing.

* You should be able to run each function by itself.

If you are doing that, then as you develop your code, you can write and run each function until it's doing what it's supposed to do, and THEN put it all together.

One way to run a function is to call it in the ``__name__ == "__main__"`` block. You can then comment and uncomment each call as you work on your code.

Also: you really, really need a way to run your code with a couple keystrokes!!

I'll demonstrate this when we review code.




looping through a dict
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


dict as switch -- how do you leave the loop?
--------------------------------------------

Let's look at a particularly nifty solution:

``solutions/Lesson05/mailroom_dict_as_switch``


quit()
------

In my solution to mailroom, I created a function called ``quit`` to quit the program. That is not a great idea, as there is a built-in called ``quit``.  In my defense, the ``quit()`` built-in didn't exist when I learned Python :-).


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

``open()`` uses text mode (deafult encoding -- utf-8?) by default. It will try to decode the file into text. If you open a binary file that way it will likely barf.

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


Testing?
--------

Did y'all do the testing exercise with a coding bat example?

We could do one now.

Or...


Advanced Argument Passing
-------------------------

All this ``*arg``, ``**kwargs`` stuff a bit confusing?

Let's explore it a bit.

AND -- we'll use TDD to do it.

Exercise in the class notes here:

:ref:`exercise_args_kwargs_lab`









