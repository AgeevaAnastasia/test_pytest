import pytest
from utils import mult_30_not_105_not_15 as mult


def test_mult():
    assert mult(40) is True


def test_mult1():
    assert mult(30) is False
