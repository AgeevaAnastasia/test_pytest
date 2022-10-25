import pytest
from utils import sum_of_pairs


@pytest.mark.parametrize('lst, expected_result', [
    ([2, 3, 4, 5, 6], [12, 15, 16]),
    ([2, 3, 5, 6], [12, 15]),
    ([3, 5, 12, 4, 9], [27, 20, 144]),
    ([13, 8, 34, 1], [13, 272])
])


def test_sum_of_pairs(lst, expected_result):
    assert sum_of_pairs(lst) == expected_result
