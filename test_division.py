# Марат, честно говоря, тут и кода-то нет, я просто скопировала то, что было на лекции для 
# проверки, как оно у меня будет работать. Так вот библиотеку установила, вроде бы, но она
# не работает pytest подчеркнуто желтой волнистой линией и написано 
# "Import "pytest" could not be resolved Pylance (reportMissingImports)"
# ну и код, конечно, не работает. 

import pytest
from utils import division

def test_division_good():
    assert division(10, 2) == 5