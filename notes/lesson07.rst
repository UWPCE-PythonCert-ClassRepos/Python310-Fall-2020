
:orphan:

.. _notes_lesson07:

#######################
11/24/2020: import this
#######################


A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

We've gotten a bit behind -- so lots of lightning talks today!

|
| Micha Park
|
| Sopheaktr L Danh
|
| Vikram Raghavan
|
| Farhan Samani
|
| Katrina Seok Taylor
|
| Bishal Gupta
|
| Maria G Berschauer
|
| Nathan Marc Debard
|

Scheduling:
===========

This is Thanksgiving week -- Are Sunday office hours still good?

If I held additional office hours, would you come?


Issues that came up during the week.
====================================

Naming Things
-------------

There's an adage in programming:

.. centered:: **Naming Things is Hard**

It really is. But it's also important. Good names for variables make the code a lot easier to read and understand.

This may seem like a non-issue when you are working on a small project. When you are in the middle of it, you know exactly what you mean when you are working with a variable called "i" or "item" or "key". But when you go read the code a week, month, year later -- and when that variable is defined somewhere off the page, you really will get confused.

And even worse are names that are just plain "wrong" (probably due to refactoring) a function called `print_something` that doesn't print anything, a variable called `donor` that is really a list of past donations, you get the idea.

Believe me, when I read your code, I really do get confused when variables don't mean what their name suggests they mean. And you will et confused as well, when you re-read the code later one -- maybe even only a week later.

Also, in a larger project, you are stuck with the names you choose up front -- at least with ones for functions and classes that will be used elsewhere. So it's really worth putting some thought into it right up front.

Style
-----

Some of you are still not following PEP 8 style. If you can't (or don't want to) set up a linter in your editor or IDE, you can run ``pycodestyle`` on your code.

https://pycodestyle.readthedocs.io

``python3 -m pip install pycodestyle``

Let's give it a quick try.


Auto-fixing style
.................

If you don't want to fix all that by hand, there are tools to do it for you.

Some options are:

AutoPEP8
........

https://pypi.org/project/autopep8/

YAPF
....

https://github.com/google/yapf

Black
.....

https://black.readthedocs.io/en/stable/

These are in order of how "opinionated" or "intrusive" they are. AutoPEP8 only fixes actual PEP8 violations. YAPF is fairly configurable as to what it does, and exactly how. Black only does one thing: make all the code in the Black style. 


  "You can have your code in any style you want -- as long as it's Black"

Adapted from the famous quote by Henry Ford about the model T:

  `"Any customer can have a car painted any color that he wants so long as it is black" <https://en.wikiquote.org/wiki/Henry_Ford>`_

Maybe give one of them a try. You can also likely plug one or the other into your editor.


Chaining ``or``, etc.
---------------------

This looks pretty nifty:

.. code-block:: python

    while answer != 'x' or 'r' or 't' or 'a':
        do_something()

But does that mean what you expect it to?

will it ever be ``False``?

Let's play with that...

Operator Precedence
...................

This table tells you which operators have "Precedence" over each other -- that is, which are evaluated first:

https://docs.python.org/3/reference/expressions.html#operator-precedence

When in doubt -- add parenthesis to make it clear. Is there any way to add parentheses that works for the above?

Comparison Chaining
...................

Another complication in all this is chaining of comparisons:

https://docs.python.org/3/reference/expressions.html#comparisons

It allows you to do nifty (and very readable) things like:

.. code-block:: python

    if a < b < c:
        do_something()

That's nice, 'cause it looks a lot like math -- simple and clear.

and it means:

.. code-block:: python

    if (a < b) and (b < c):
        do_something()


So with chaining, you can't just add parentheses to make it clear.

Also -- like with ``and`` and ``or``, chaining "shortcuts".  In the example above, if ``a`` is not less than ``b``, then ``c`` will never be evaluated. And ``b`` will only be evaluated once in any case.

So what's going on here?

.. code-block:: ipython

    In [41]: 2 < 5 in range(3)
    Out[41]: False

    In [42]: (2 < 5) in range(3)
    Out[42]: True

    In [43]: 2 < (5 in range(3))
    Out[43]: False


Turns out that ``in``, ``not``, ``not in`` are considered comparison operators too (at least in this context)


Mutating vs. re-assigning
-------------------------

I've seen code like this in a few trigram solutions:

``output = output + [follower]``

(``output`` is a list of strings, follower is a single string)

What it does is add a new item to a list.

But is that an efficient way to do that?

If you are adding one element to a list -- ``append()`` is the way to go.

``output_list.append(random_trigram_followers)``

Using addition works fine, but it's creating a whole new list (actually: *two* new lists) just to throw it away again.

And if you are adding another list of objects, you want to use ``extend()``.

With this code:

``output = output + [follower]``

This is what happens:

1) Create a one-element list with ``follower`` in it.
2) Create a new list with the contents of ``output`` and that just created list.
3) Re-assign the name ``output`` to that new list.
4) Throw away the original list ``output`` was bound to, and the temporary list created for ``follower``.

That's a LOT of overhead!

mutating vs assigning
.....................

Be cognizant of when you are mutating (changing) an object vs. creating a new one and assigning it to the same name. When you do assignment (``=``) you are probably creating a new object -- is that what you want? And if you are NOT using ``=``, then you are probably mutating an existing object.

``+=`` is different -- it is the "in_place" operator, so:

``a_list += another_list``

does not create an new list -- it adds to the original list "in place" -- it is identical to:

``a_list.extend(another_list)``

And it is an efficient operation.

The trick is that the "augmented assignment" operators, like ``+=`` **do** create new object when used with an immutable:

.. code-block:: ipython

    In [4]: tup1 = tup2 = (1, 2, 3)

    In [5]: tup1 is tup2
    Out[5]: True

    In [6]: tup1 += (4, 5)

    In [7]: tup1 is tup2
    Out[7]: False

    In [9]: tup1
    Out[9]: (1, 2, 3, 4, 5)

    In [10]: tup2
    Out[10]: (1, 2, 3)

Contrast this with (mutable) lists:

.. code-block:: ipython

    In [11]: list1 = list2 = [1, 2, 3]

    In [12]: list1 += [3, 4]

    In [13]: list1 is list2
    Out[13]: True

    In [14]: list1
    Out[14]: [1, 2, 3, 3, 4]

    In [15]: list2
    Out[15]: [1, 2, 3, 3, 4]

Personally, I think it's a "wart" that augmented assignment may or may not be a mutating operation.

But at the time it was added, there were two goals:

1) Efficient in-place operations on mutables (partly to support numpy)

2) Quick and easy incrementing of values, in particular integers:

``i += 1``

And no one wanted to add **two** new sets of operators.

https://www.python.org/dev/peps/pep-0203/

What to return?
---------------

It is a convention in Python to return a new object if one is created (kind of necessary, actually), but to return ``None`` if a new object is NOT created -- i.e. the existing object is mutated. Contrast strings and lists:

Strings are immutable, so they can't be changed in place:

.. code-block:: ipython

    In [11]: a_string = "this is a string"

    In [12]: new_string = a_string.capitalize()

    In [13]: print(new_string)
    This is a string

    In [14]: print(a_string)
    this is a string

Whereas lists are mutable, and they CAN be changed in place:

.. code-block:: ipython

    In [15]: a_list = [4, 2, 8, 3, 9, 1, 4]

    In [16]: new_list = a_list.sort()

    In [17]: print(new_list)
    None

    In [18]: print(a_list)
    [1, 2, 3, 4, 4, 8, 9]

note that the mutating method, ``.sort()`` returns ``None``. This makes it a bit annoying sometimes, as you can't chain operations, but it also makes it less confusing.

This is a standard practice in the Python standard library, but you really should follow it in your own code:

.. code-block:: python

    def add_donor(new_donor):
        """
        add a new donor to the global donor database
        """
        ...
        return None

This REALLY should not return the global donor database.

Similarly, if a function takes a mutable on input, and changes it in place, it should not return the passed-in object:


.. code-block:: python

    def add_donation(donor, donation):
        """
        add a new donation to a donor
        
        :param donor: the donor object to add the donation to

        :param donation: the donation to add
        """

        donor[1].append(donation)

        # don't do this!!!!
        return donor

This should return ``None`` to indicate that the passed-in donor object was changed in place.


Break -- Then Lightning Talks
=============================


| Micha Park
|
| Sopheaktr L Danh
|
| Vikram Raghavan
|
| Farhan Samani
|

Packaging
=========

Are you all thoroughly confused now?

There are a number of subtleties here: 


relative importing
------------------

what the heck does:

``from .mailroom import model as m``

mean?

What about:

``from ..mailroom.cli import main`` ?


Where does Python look for modules and packages?
------------------------------------------------

``sys.path``: let's take a look.

Note that the current working directory is put on sys,path by default -- what are the implications of that?

what about scripts??
--------------------

It turns out that the "old" ``scripts`` keyword to ``setup()`` is not totally reliable (particularly on Windows). And it can cause some complications. I always liked the simplicity of scripts, but it really is a better idea to use setuptools' console_scripts entry point. 

But the errors we saw are instructive -- so let's take a look. In particular, what happens when you have a script with the same name as your package?


Let's take a look at my packaged up mailroom to see how that works.

args and kwargs
===============

Python's very flexible parameter specification and argument passing is really powerful, but it can be confusing: 

Any particular confusions?

What to look at my ``*args, **kwargs`` Lab?



Break -- Then Lightning Talks
=============================

|
| Katrina Seok Taylor
|
| Bishal Gupta
|
| Maria G Berschauer
|
| Nathan Marc Debard
|


Any other questions/issues before we get into classes?
------------------------------------------------------

Note that we'll be employing packaging and testing the rest of the class, so if you don't quite "get it",  you'll have more chances :-)


Classes!
========

Classes are the core of Object Oriented programming. Rather than talk about them in the abstract, we'll start doing a real problem, and talk about the pieces as we go.

So: on to the Object oriented intro!

https://uwpce-pythoncert.github.io/ProgrammingInPython/exercises/oo_intro/oo_intro.html








