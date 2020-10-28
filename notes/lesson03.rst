:orphan:

.. _notes_lesson03:

####################
Notes for lesson 03
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Up today:

From last week:

Jason Emmett Hill


And then:

Jimmy Nguyen

Brian H Wong

Arielle Waller (Ari)

Erik J Knighton


Are you ready? We'll do them in the middle of the lesson.

Issues that came up during the week.
====================================

gitHub "Failures"
-----------------

Sorry about that -- that's a "linter", set up to check style issues. I've turned it off for teh next few assignments.


main or master?
---------------

the default branch for git (and gitHub) used be called master. Soyou will see a LOT of docs talking abou tthe master branch. But gitHub now uses "main" for the default branch. Most of our TEmplate repos for the class were created before they made the switch, so the default branch is called "master". But you may start seeing "main" used too.

The key point is that he name of the branch is arbitrary, the only special about "main" or "master" is that it is the default branch. Other than that, it, or any other branch, could be called anything.


git chaos!
----------

If you have somethign wierd going on with git, there are a few options:

- Google it -- there is a LOT of infomation about git online.

- Too much information, we have some git hints that might help you out of a jam for this class:

https://uwpce-pythoncert.github.io/ProgrammingInPython/topics/01-setting_up/git_hints.html

**If all else fails:**

One of the great things about git is that is a "distributed" version control system. That means that every copy (clone) of a repository has all teh information in it. And what that means is that if the clone on your workstation gets in a mess -- you can smiply make another clone from gitHub and start again. If you move or rename the old (confused) one -- then all the files in it will still be there, so you can copy any of your work that had not been pushed to gitHub over to the new clone.


git commit and PR messages
--------------------------

At this poiint, it's pretty obvious what you are doing. But as the projects get more complicated, it won't be.

So please put meaningful commit and PR messages -- particularly PR messages!

This is a **really good** habit to get into for future development work.



PEP08 and a linter
------------------

It is a really good idea to get in the habit of using consistent style in your code -- i.e. follow PEP08.

And this is really easy to do if you have a linter set up in your editor. If you haven't gotten that to work -- do try to do so soon!

https://www.python.org/dev/peps/pep-0008/

Even more important that all of that:

**Use four spaces per indent**

**ALWAYS**

What's a docstring ?
--------------------



``if __name__ == __main__``
---------------------------

What's *that* all about?

Note: There's a video in Lesson 2 -- anyone still confused?

What is a ``range()`` object?
-----------------------------

What does range actually create? Let's check it out!


triple quoted strings or comments?
----------------------------------

It's not a good practice to use triple qluoted streings to "comment out" blocks of code.

Use comments:

# this is a line of code
# and this is another
# and one more.

Your editor / IDE should make that easy!


Separation of Concerns
----------------------

From print_grid: if you are going to have separate functions, better for them to return a string, and then put all the printing in the calling function, in one place. That would make it more re-usable -- say you want to write to a file?

This is a tiny example of what's known as "separation of concerns"

``for`` vs ``while``
--------------------

Quite a few folks used a ``while`` loop in ``print_grid``,
and ``sum_series``, and ...

But for all these cases, a ``for`` loop (and ``range()``) is a better option.

So: When to use ``for`` vs ``while`` ?

* You can do everything with a ``while`` loop -- you never actually *need* ``for``

But:

``for`` is pretty handy primarily for looping through the items in an iterable -- doing the similar things to everything in a collection.

And ``range()`` is an easy-to-create collection of a sequence of integers of a given size.

So in short:

Use ``while`` when you want to repeat something some unknown number of times -- maybe a few times maybe thousands...

Use ``for`` when you want to work with an entire collection, or a pre-determined number of loops.


``is`` vs ``==``
----------------

In FizzBuzz, someone had code something like this:

```
if n % 3 is 0:
```

That works, but it's a "Bad Idea™"

"is" tests whether the objects are actually the same object -- not whether they have the same value. As you can easily have multiple objects that happen to have the same value, "is" will fail in the general case.

But why did it work there?

This works because cpython has an optimization called "interning" -- since small integers are used so often, the interpreter keeps a pool of them around to re-use, rather than creating multiple integer objects with the same value.

So "is" will work as a test for small integers, but not large ones:

.. code-block:: ipython

    In [65]: x = 5

    In [66]: y = 5

    In [67]: x is y
    Out[67]: True

    In [68]: x = 345678

    In [69]: y = 345678

    In [70]: x is y
    Out[70]: False

**NOTE:** This is also the case for small strings.

**Important:** This is an implementation detail. Do not count on it!


Review Solutions
================

I've posted my solutions to last week's assignments in the class repo::

  git pull

They are in::

  solutions/Lesson02

But before we do that -- code review / refactoring:
Angela -- can we look at your code?



Lightning Talks
===============

Let's take a break and do the  lightning talks...


Jason Hill

Jimmy Nguyen

Brian H Wong

Ari Waller

Erik J Knighton


Now some new stuff
==================

Labs:
-----

Get a start on your own, then we'll come together and finish it up.

:ref:`exercise_slicing`

:ref:`exercise_list_lab`

:ref:`exercise_string_formatting`

Mailroom
--------

Let's start this as a group:

:ref:`exercise_mailroom_part1`






