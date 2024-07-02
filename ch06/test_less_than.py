import cards
import pytest
from cards import Card
from packaging.version import parse

@pytest.mark.skip(reason='operator < is not yet supported')
def test_less_than():
    c1 = Card('a task')
    c2 = Card('b task')
    assert c1 < c2

@pytest.mark.skipif(parse(cards.__version__).major < 2, reason='operator < not supported in version 1.x')
def test_less_than2():
    c1 = Card('a task')
    c2 = Card('b task')
    assert c1 < c2
