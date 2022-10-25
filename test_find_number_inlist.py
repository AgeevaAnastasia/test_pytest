import pytest
from utils import find_number_inlist


def test_f():
    assert find_number_inlist(['df', '3', 'sdfs'], '3') is True


def test_neg():
    assert find_number_inlist(['df', '3', 'sdfs'], '4') is None
