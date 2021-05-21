from ._financial_modeling import *


__version__ = "0.0.2"
__all__ = ["ar", "lr", "aar", "twr", "an", "pv", "npv", "gm"]

# module level doc-string
__doc__ = """
financial-modeling - a simple financial modeling library for Python
=====================================================================
**financial** is a Python package providing simple, easy to undestand, and useful
library designed to make people lives a little easier when dealing with financial
modeling using Python. At the moment it aims to be easy enough so people feel home when 
using it. Additionally, it has the broader goal of becoming **the goto library when people
consider doing financial modeling in Python**. It is already well on its way toward this 
goal.

Main Features
-------------
Here are just a few of the things that ``financial_modeling`` has at the moment:
  - A list of necessary rate of returns functions ready to be used 
  - Easy to undestand code base so anyone can contribute to.
  - Enough documentation to get you started.
  - Full test coverage so everything is checked before adding/changing functionality
"""