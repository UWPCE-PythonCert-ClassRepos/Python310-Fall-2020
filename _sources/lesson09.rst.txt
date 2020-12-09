
:orphan:

.. _notes_lesson09:

###############################################
Dec 8, 2020: Around around and around we go ...
###############################################


A collection of notes to go over in class, to keep things organized.


Lightning Talks
===============

Christopher Duane Smith

Maria Corazon M Dacutanan

Akalpit Gadre

Roohie Menon


Issues that came up during the week.
====================================

classmethods
------------

You really want to use the  ``cls`` parameter in a classmethod::

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return Circle(radius)

should be::

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

Why? Subclassing!

Let's play with that a bit ....


NotImplemented
--------------

``NotImplemented`` is a special value that can be used as a flag to indicate that a comparison cannot be made.

https://docs.python.org/3/library/constants.html?highlight=notimplemented#NotImplemented


Total Ordering?!?
-----------------

What does that mean?

"Total Order" is a mathematical concept that's a bit beyond me :-)

But the layperson's version is simply that two things are either less than, equal, or greater than each other in a consistent way.

And what *that* means is that if you define equality, and one of less-than or greater-than, the others can all be derived from those two.

So that is what the ``functools.total_ordering`` decorator does: it automatically creates the full set of comparison operators in terms if the two provided.

Let's take a quick look at my solution to see how that works.


``sum()``
---------

You can use ``sum()`` for things other than numbers. Anything that you can add, you can use ``sum()`` for, but you need to give it a "start" value. You can use sum() on circles if you want::

.. code-block:: ipython

    In [16]: sum([Circle(2), Circle(3), Circle(4)], start=Circle(0))
    Out[16]: Circle(9.0)

Or from trigrams:

.. code-block:: ipython

    In [14]: text
    Out[14]:
    ['him mention her under any other name. In his eyes she eclipses',
     'and predominates the whole of her sex. It was not that he felt',
     'any emotion akin to love for Irene Adler. All emotions, and that']

    In [15]: sum((line.split() for line in text), [])
    Out[15]:
    ['him',
     'mention',
     'her',
     'under',
     'any',
     'other',
     'name.',
     ...

Except not strings (note the above is lists of strings, not strings themselves):

.. code-block:: ipython

    In [17]: sum(["this", "that", "something"], "")
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-17-c882ae453790> in <module>
    ----> 1 sum(["this", "that", "something"], "")

    TypeError: sum() can't sum strings [use ''.join(seq) instead]

That's because ``.join()`` is a lot more efficient.


"private" attributes and dunders
--------------------------------

``_something`` vs ``__something`` vs ``__something__``

Let's talk about that...





Magic Methods and Circle class
------------------------------

Any questions?

Should we look at mine?


Lightning Talks
===============


Christopher Duane Smith

Maria Corazon M Dacutanan

Akalpit Gadre

Roohie Menon


New Topics
==========

sorting
-------

maybe it's a good idea to add a sort_key method to your classes?

see ``examples/lesson09/sort_key.py``

let's try it on Circle....

OO Design
---------

You can find a lot of stuff written about OO design. I am a bit wary of much of it -- I think we should all follow good design practices, and use OO features when they are useful, not because they follow from a OO design process. That being said, here are a few thoughts:

**Nouns vs Verbs:**

  - Nouns are classes (Donor, Circle, ....)
  - Verbs are are methods.

But you don't need to make a class just because you have a noun: nouns can be simple data types as well: a string, and integer, a list ....

And you **Really don't** want to make a class, just so you can then add a method to it to make a verb! Simple things can be simple, if a function does one thing, with simple inputs, and simiple outputs, it can just be a function.

This is why ``staticmethod`` is not used much in Python -- if it's a static method, why put it in a class? Just make it a function!

I really like Jack Dietrich's point:

  "If a class only has two methods, and one of them is __init__, you don't have a class"

**Encapsulation:**

Encapsulation is keeping things "hidden" -- many folks (and languages) see this as an important feature. But Python doesn't strictly support it at all. However, it IS a good idea to keep the data, and the methods that act on that data together. Not because we need to hide tings, but because then there is a single clear API to work with, and the under the hood details can be changed without breaking other code. Classes are helpful for this.

**Keeping it DRY**

  Don't Repeat Yourself!

This is THE BIG ONE in program  design -- it drives a lot of design decisions. When you realy want classes is when:

1) you are going to make a lot of instances of the class

and/or

2) you are going to subclass

We really haven't done much subclassing yet -- but you'll see how that can really help keep your code DRY.

**Separation of Concerns:**

This is keeping thinks well grouped so that code that does the same thing stays together. It's not strictly required to use classes for that -- but it does help.

Thoughts, ideas?

Let's keep these things in mind as we think about how (and whether) to restructure Mailroom with classes.


Object Oriented Mailroom
------------------------

One more time!

Yes, it's time to make mailroom Object Oriented:

:ref:`exercise_mailroom_oo`







