"""
this version tests the solution with slicing tests
"""


import pytest
from sparse_array import SparseArray


def set_up():
    my_array = [2, 0, 0, 0, 3, 0, 0, 0, 4, 5, 6, 0, 2, 9]
    my_sparse = SparseArray(my_array)
    return (my_array, my_sparse)


def test_object_exists():
    my_array, my_sparse = set_up()
    assert isinstance(my_sparse, SparseArray)


def test_not_equal_list():
    my_array, my_sparse = set_up()
    assert not my_array == my_sparse


def test_not_equal_values():
    assert (SparseArray([2, 5, 0, 2, 0, 0, 0, 0, 1]) !=
            SparseArray([2, 5, 0, 2, 0, 0, 1, 0, 1]))


def test_not_equal_length():
    assert (SparseArray([2, 5, 0, 2, 0, 0, 0, 0, 1]) !=
            SparseArray([2, 5, 0, 2, 0, 0, 0, 0, 1, 0, 0]))


def test_equal():
    assert (SparseArray([2, 5, 0, 2, 0, 0, 0, 0, 1]) ==
            SparseArray([2, 5, 0, 2, 0, 0, 0, 0, 1]))


def test_get_non_zero_number():
    my_array, my_sparse = set_up()
    assert my_sparse[4] == 3


def test_get_zero():
    my_array, my_sparse = set_up()
    assert my_sparse[1] == 0


def test_get_element_not_in_array():
    my_array, my_sparse = set_up()
    with pytest.raises(IndexError):
        my_sparse[14]


def test_str():
    my_sparse = SparseArray([0, 3, 12, 0, 0])
    print(my_sparse)
    assert str(my_sparse) == "SparseArray([0, 3, 12, 0, 0])"


def test_repr():
    my_array, my_sparse = set_up()
    assert my_sparse == eval(repr(my_sparse))


def test_get_slice():
    my_array, my_sparse = set_up()
    assert my_sparse[2:4] == SparseArray([0, 0])


def test_set_slice_over():
    my_array, my_sparse = set_up()
    my_sparse[13:17] = [5, 3, 4]
    assert my_sparse == SparseArray([2, 0, 0, 0, 3, 0, 0, 0, 4, 5, 6, 0, 2, 5, 3, 4])


def test_set_slice_insert():
    # inserting a larger slice
    my_array, my_sparse = set_up()
    my_sparse[2:4] = [2, 3, 4]
    assert my_sparse == SparseArray([2, 0, 2, 3, 4, 3, 0, 0, 0, 4, 5, 6, 0, 2, 9])


def test_get_length():
    my_array, my_sparse = set_up()
    assert len(my_sparse) == 14


def test_change_number_in_array():
    my_array, my_sparse = set_up()
    my_sparse[0] = 3
    assert my_sparse[0] == 3
    # make sure others aren't changed
    assert my_sparse[1] == 0
    # make sure still same length
    assert len(my_sparse) == 14


def test_change_number_in_array_to_zero():
    my_array, my_sparse = set_up()
    my_sparse[4] = 0
    assert my_sparse[4] == 0
    # make sure still same length
    assert len(my_sparse) == 14


def test_change_number_in_array_from_zero():
    my_array, my_sparse = set_up()
    my_sparse[1] = 4
    assert my_sparse[1] == 4
    # make sure still same length
    assert len(my_sparse) == 14


def test_change_slice():
    my_array, my_sparse = set_up()
    my_sparse[1:3] = [2, 3]
    assert my_sparse[1:3] == SparseArray([2, 3])


def test_delete_number():
    my_array, my_sparse = set_up()
    del(my_sparse[4])
    # if we delete the 4 position, should now be zero
    assert my_sparse[4] == 0
    # should have smaller length
    assert len(my_sparse) == 13


def test_delete_zero():
    my_array, my_sparse = set_up()
    del my_sparse[5]
    # should still be zero, but should have shorter length
    assert my_sparse[5] == 0
    assert len(my_sparse) == 13


def test_delete_last_number():
    my_array, my_sparse = set_up()
    del(my_sparse[13])
    # should get an error
    with pytest.raises(IndexError):
        my_sparse[13]
    assert len(my_sparse) == 13


def test_indices_change():
    my_array, my_sparse = set_up()
    del(my_sparse[3])
    # next index should have changed
    # my_sparse[4] was 3 now
    # my_sparse[3] should be 3
    assert (my_sparse[3] == 3)


def test_iteration():
    """
    can it be iterated through?
    """
    my_array, my_sparse = set_up()

    # use in a list comp:
    result = [i for i in my_sparse]

    assert result == my_array


