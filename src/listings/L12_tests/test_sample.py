"""Exampling showing function definition and test in a single file."""

# author:   Thomas Haslwanter
# date:     April-2021


def inc(x):
    """The function to be tested. Increments inputs by 1."""
    return x + 1


def test_answer():
    """The test to check that the function 'inc' provides the correct result."""
    assert inc(3) == 4
