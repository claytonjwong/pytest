import pytest
from cards import Card

@pytest.mark.skip(reason='operator < is not yet supported')
def test_less_than():
    c1 = Card('a task')
    c2 = Card('b task')
    assert c1 < c2
