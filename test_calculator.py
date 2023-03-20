import pytest

from calculator import Calculator

#from calculator import add_two_numb, Calculator

assert isinstance(pytest.mark.math, object)


@pytest.mark.math
@pytest.mark.math_add
def test_add_single_digit_nums():
    object = Calculator()
    result = object.add_two_numb(2, 3)
    #result = Calculator().add_two_numb(2, 3)
    assert result == 5, "sum of 2+3 should be 5"

'''
@pytest.mark.math
@pytest.mark.math_add
def test_add_double_digit_nums():
    result = Calculator().add_two_numb(20, 30)
    assert result == 50, "sum of 20+30 should be 600"


@pytest.mark.math
@pytest.mark.math_mul
def test_multiply_single_digit_nums():
    result = Calculator().multiply_two_numb(2, 3)
    assert result == 6, "sum of 2*3 should be 6"


@pytest.mark.math
@pytest.mark.math_mul
def test_multiply_double_digit_nums():
    result = Calculator().multiply_two_numb(20, 30)
    assert result == 600, "sum of 20*30 should be 600" '''
