.. Malee documentation master file, created by
   sphinx-quickstart on Thu Jun  3 00:31:41 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Malee's documentation!
=================================
The ``malee`` package contains a collection of financial modeling functions.

The major goal of this package is to provide you an easy to use library that 
implements most of the financial modeling formulas like risk and return ready 
to be used. This package is using ``numpy`` as its backend so everything is fast 
enough as you might expect. There are similar projects like `numpy-financial 
<https://github.com/numpy/numpy-financial>`_, but most of the have these two problems 
of 1) not having everything you might need 2) not being maintained actively. Hence this 
packages aims to fill this gap and be your goto library when you want financial modeling stuff.

``malee`` in Farsi means *Financial*. Tried so many other cool names, but I was late in the game
and they were already taken.

The source code of this package is available at https://github.com/RezaBehzadpour/malee

Installation
############
You can easily install this package by typing the following command
in your terminal:

.. code-block:: bash

      $ pip install malee

How to use it?
##############
Here's a simple example of how you can calcualate Artihmetic Rate of
Return using ``malee``:

.. code-block:: python

      >>> import malee
      >>> malee.ar(100, 140)
      0.4

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
