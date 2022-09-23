#!/usr/bin/env python3
"""
Test the Scraper class.
"""

__author__ = "Jason Beach"
__version__ = "0.1.0"
__license__ = "MIT"


import sys
from pathlib import Path
from graphipy.graph.graph_pandas import PandasGraph


def test_init():
    pg = PandasGraph()
    assert True == True