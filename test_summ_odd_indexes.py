import pytest
from utils import summ_odd_indexes as summ



def test_summ():
    assert summ([2, 3, 5, 9, 3]) == 12
