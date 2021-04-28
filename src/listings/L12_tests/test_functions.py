""" This module contains the test-function for the module 'functions.py' """

# author:   Thomas Haslwanter
# date:     April-2021

import functions as fcn


def test_inc():
    """The test to check that the function 'inc' provides the correct result."""
    assert fcn.inc(4)==5


def test_dec():
    """The test to check that the function 'dec' provides the correct result."""
    assert fcn.dec(4)==3
