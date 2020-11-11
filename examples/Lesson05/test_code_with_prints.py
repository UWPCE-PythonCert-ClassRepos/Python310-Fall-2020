"""
how to test printing in functions

which you should RARELY need to do!
"""
# from pytest import capsys

from code_with_prints import (really_simple,
                              almost_as_simple,
                              )


def test_simple_wrong():
    # first just call it
    assert really_simple() == "just this"

    # assert really_simple() == print("just this")


#  the way to do it is to use a pytest fixture:
# https://docs.pytest.org/en/stable/capture.html#accessing-captured-output-from-a-test-function


# def test_almost_as_simple(capsys):
#     # call the print function
#     almost_as_simple(3)

#     # check the results:
#     captured = capsys.readouterr()
#     assert captured.out == "-*--*--*-\n"




