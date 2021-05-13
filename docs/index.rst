.. Finacial Modeling documentation master file, created by
   sphinx-quickstart on Sat May  8 02:58:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Finacial Modeling's documentation!
=============================================

*Financial Modeling in Python made simple.*

The ``financial_modeling`` Python package is a collection of 
essential financial modeling functions. I wrote this package 
for my master's degree to make my life and my classmates a 
little easier and help others use it for educational and 
academic use cases. It's not meant to be used for production 
environments yet. I intentionally didn't use `numpy` as the 
backend for calculations to make the code easy enough for 
everyone to understand and develop if needed.

Installation
############
You can easily install this package by typing the following command
in your terminal:

.. code-block:: bash

      $ pip install -U financial_modeling

How to use it?
##############
Here's a simple example of how you can calcualate Artihmetic Rate of
Return using ``financial_modeling``:

.. code-block:: python

      >>> import financial_modeling as fm
      >>> fm.ar(100, 140)
      0.4


For more information and see the full API, please refer to the
package documentation_ or head over to the next section.

.. _documentation: financial_modeling.html#module-financial_modeling

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
