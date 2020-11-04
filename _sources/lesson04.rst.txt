:orphan:

.. _notes_lesson04:

#############################
11/02/2020: A actual Program!
#############################


A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

| Quinn Yackulic
|
| Kelly Kauffman
|
| James Roefs
|
| Jonathan Paul Bednar
|
| Jeff Bennett


As usual, these notes are published here:

https://uwpce-pythoncert-classrepos.github.io/Python310-Fall-2020/

And the Solutions are in teh gitHub project:

https://github.com/UWPCE-PythonCert-ClassRepos/Python310-Fall-2020


Quick Poll: how many of you have a clone of that repo on your machine?


Issues that came up during the week.
====================================

Style
-----

Use PEP8 style -- really!

https://www.python.org/dev/peps/pep-0008/

The ONLY exception is if you work in an organization that has a different style guide. It can make sense for your python code to match other code in an organization. But otherwise, use a style consistent with the rest of the Python world.

The best way to do this is with a linter in your editor -- like the Anaconda package in Sublime. If you are getting annoyed by all the "noise" that the linter creates -- keep your code in PEP8 style, it won't be there!

And don't use "Hungarian Notation" -- it is really non-pythonic, and sometimes actually wrong -- and a string called ``intSomething`` just adds confusion!


Also: use meaningful names, not "item" or "tup" or ....


Built in names
--------------

Python has a number of "key words" that are reserved. If you try to use them as a variable name, you will get an error:

.. code-block:: ipython

    In [1]: for = 5
      File "<ipython-input-1-36df406aa65d>", line 1
        for = 5
            ^
    SyntaxError: invalid syntax

Sometimes a bit confusing, as it's not REALLY a syntax error, but rather using a keyword as a variable....

But there are also a LOT of "built in" names. Try::

    dir(__builtins__)

You can use these names for a variable, but when you do, it will write over the built-in one, which means that you then can't use it in the usual way. For instance, ``list`` is the list type, you can make a list out of any sequence with it:

.. code-block:: ipython

    In [6]: list("this")
    Out[6]: ['t', 'h', 'i', 's']

But if you use it as a name, it then won't work in the usual way:

.. code-block:: ipython

    In [7]: list = [1, 2, 3, 4, 5]

    In [8]: list
    Out[8]: [1, 2, 3, 4, 5]

    In [9]: list("this")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-9-c89f7438771a> in <module>()
    ----> 1 list("this")

    TypeError: 'list' object is not callable

Moral of the story:

**Don't "shadow" built in names**

Use things like::

    my_list
    infile

or even misspellings or adding an underscore:

``klass`` or ``cls`` or ``_class`` instead of ``class``

Hopefully your editor will warn you -- otherwise, think about it when you get a strange error like:

.. code-block:: ipython

    In [14]: input = "this was some input"

    In [15]: input("=>")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-15-56a225daeb09> in <module>()
    ----> 1 input("=>")

    TypeError: 'str' object is not callable


Mutable default parameters
--------------------------

There was a video on this -- any questions about it?

If not then we'll move on ...

But if you are confused ....

This is a real "gotcha" in Python. Someone (in a previous class) wrote a non-recursive solution to the sum_series problem. It worked great -- EXCEPT if it got called more than once! Any idea what the problem is?

(``examples\lesson04\series_with_mutable.py``)

.. code-block:: python

    def sum_series(nth=1, sequence=[0,1]):
        """
        Generate a list of sums given a seed and return the Nth number.
        """
        for i in range(2, nth):
            sequence.append(sequence[i-2] + sequence[i-1])
        return sequence[nth-1]

So this uses the logic of starting out with the first two values in the series, and then looping to build up the series from there.

And [0, 1] is set as a default to start the series off -- the start of the Fibonacci series.  So if you pass in only one argument, you should get the Fibonacci number:

Remember that the start of the Fibonacci series is::

  0, 1, 1, 2, 3, 5, 8, 13, ...

What happens when you run this code:

.. code-block:: python

    In [21]: sum_series(5)
    Out[21]: 3

All good.

    In [22]: sum_series(6)
    Out[22]: 1
    # WTF???

The issue is that:

Default Arguments get evaluated **when the function is defined**. So every time the function is called, it will use the *same* list! Each time adding more and more to the list.

Let's explore that some more, and some solutions....


Recursion in an interactive loop
--------------------------------

Not a great idea!

you can do something like:

.. code-block:: python

    def mainloop():
        while True:
            ans = input("A question > ")
            ....
            if ans == "again"
                mainloop()

Let's look at this:

``examples/lesson04/recursive_mainloop.py``

(do a ``git pull`` if you have a clone of the class repo)


Lightning Talks
===============

let's take a break, and then:

| Quinn Yackulic
|
| Kelly Kauffman
|
| James Roefs


Slicing and List labs
---------------------

Any questions?


Altering a list while looping through it
........................................

what could go wrong with this code?

.. code-block:: python

    for i in a_list:
        if some_condition:
            a_list.remove(i)

Let's try it out ...

``examples/lesson04/deleting_in_loop.py``

Sorting
.......

Anyone confused about sorting? Shall we go over it?

``examples/lesson04/sort_example.py``


String Formatting
-----------------

Are you starting to get it? There is a LOT there. But it lets you do some fancy stuff with not much code.


My solutions
------------

Let's look at some solutions quickly.

mailroom
........

Anyone get it done?

Should we look at my solution -- or review one of yours?

Or wait ?


Lightning Talks
===============

| Jonathan Paul Bednar
|
| Jeff Bennett



New Material
============

Any questions on

Unit Testing or Exceptions?

(we'll start some in class)


Unit Testing and TDD
--------------------

Compared to most Python courses, we are introducing unit testing really early. In fact, earlier that we used to in this class, which was already early.

But it is a REALLY good habit to get into, and, in fact, can help beginners just  as much (maybe more) than more experienced developers. 


Exceptions
----------

Let's do the Exceptions Lab in class:

https://uwpce-pythoncert.github.io/ProgrammingInPython/exercises/exceptions/exceptions_lab.html


Testing Mailroom 
----------------

Key point here: 

You **will** need to refactor your code in order to make it testable.

That is a "Good Thing"

Well structured code is testable : testable code is (Probably) well structured.

This is one reason we're introducing unit tests right now.

Shall we get a start on that together?


