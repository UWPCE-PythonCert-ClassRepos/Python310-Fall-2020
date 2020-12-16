
:orphan:

.. _notes_lesson10:

#############################
Dec 15, 2020: the final hour!
#############################


Lightning Talks
===============

Jin Han

Scott Guyton

Andrew Hanson


And if I've missed anyone -- now's your last chance!


Issues that came up during the week.
====================================

When to make a method vs. a property?
-------------------------------------

It is a good idea to make a property to access information in your class that requires "inside information", For example, in a Donor class:

.. code-block:: python

  @property
  def maxdonation(self):
      return max(self.donations)

This way, client code can get the maximum donation without knowing, or caring, how the donations are stored in the class.

However, there is no need to create a property to "hide" something that is already part of the public API:

.. code-block:: python

  @property
  def namelength(self):
      return(len(self.name))

There is no point to this -- ``a_donor.name`` is expected to be a string -- so if you want to know how long it is, you can simply do:  ``len(a_donor.name)``

You *do* want to use properties to "hide" implementation details -- but the name attribute being a string is part of the API, not an implementation detail.


Pointless properties
--------------------

What's wrong this?

.. code-block:: python

    class circle():
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            return self._radius
        @radius.setter
        def radius(self, radius):
            self._radius = radius



Anything else from OO mailroom?
-------------------------------

I'll take any burning questions, but want time to workon the the HTML render assignment


Lightning Talks
===============

Jin Han

Scott Guyton

Andrew Hanson


.. Do you always need an ``__init__``?
.. -----------------------------------

.. No -- you don't :-)

.. The ONLY thing "special" about ``__init__`` is that it is automatically called when an instance is created.  Other than that, it's a regular method. So if you don't define one, then the superclass' ``__init__`` will be called. (and ``object``, the default superclass, has a default one -- so it's always there somewhere).

.. That's what inheritance is all about -- the subclass inherits ALL the superclasses' methods -- including ``__init__``.

.. So never write an ``__init__`` that does nothing but call the superclass ``__init__``

.. Subclasses and ``self``
.. -----------------------

.. ``self`` is the first parameter in all methods. But why??

.. ``self`` is the "current" instance of the object. This means that you don't know at code writing time what type it is -- is it the current class? some subclass?

.. Let's experiment with that.

html_render
-----------

This one is pretty challenging -- and gets into some nifty subclassing.

So let's get a good start on it by working through it together.




The Next Class
==============

Next quarter, you'll finish up the core of the Python language, then go into depth on some of the more advanced features of the language. Finally, you'll do a bit with using Python with other tools, such as databases.


End of Quarter:
===============

"Grades" are due a week from today - as we need time to review, do try to get everything submitted by the end of Sunday.






