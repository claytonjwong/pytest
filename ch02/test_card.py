from cards import Card

def test_field_access():
    c = Card('something', 'brian', 'todo', 123)
    assert c.summary == 'something'
    assert c.owner == 'brian'
    assert c.state == 'todo'
    assert c.id == 123

def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == 'todo'
    assert c.id is None

def test_equality():
    c1 = Card('something', 'brian', 'todo', 123)
    c2 = Card('something', 'brian', 'todo', 123)
    assert c1 == c2

def test_equality_with_diff_ids():
    c1 = Card('something', 'brian', 'todo', 123)
    c2 = Card('something', 'brian', 'todo', 456)
    assert c1 == c2

def test_inequality():
    c1 = Card('something', 'brian', 'todo', 123)
    c2 = Card('something else', 'charlie', 'done', 456)
    assert c1 != c2

def test_from_dict():
    c1 = Card('something', 'brian', 'todo', 123)
    c2_dict = {
        'summary': 'something',
        'owner': 'brian',
        'state': 'todo',
        'id': 123
    }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2

def test_to_dict():
    c1 = Card('something', 'brian', 'todo', 123)
    c2 = c1.to_dict()
    c2_expected = {
        'summary': 'something',
        'owner': 'brian',
        'state': 'todo',
        'id': 123
    }
    assert c2 == c2_expected

#
# assertion helper functions
#
import pytest

def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True
    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail(f'different ids: {c1.id} != {c2.id}')

def test_identical():
    c1 = Card('foo', id=123)
    c2 = Card('foo', id=123)
    assert_identical(c1, c2)

# def test_identical_fail():
#     c1 = Card('foo', id=123)
#     c2 = Card('foo', id=456)
#     assert_identical(c1, c2)

#
# testing for expected exceptions
#
import cards

def test_no_path_fail():
    with pytest.raises(TypeError):
        cards.CardsDB()

def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exec_info:
        cards.CardsDB()
    expected = 'missing 1 required positional argument'
    assert expected in str(exec_info.value)

#
# structuring test functions
#

# given, when, then
# arrange, act, assert

# Given/Arrange - a starting state.  This is where you set up data or the environment to get ready for the action
# When/Act - some action is peformed.  This is the focus of the test - the behavior we are trying to make sure is working right
# Then/Assert - some expected result or end state should happen.  At the end of the test, we make sure the action resulted in the expected behavior

def test_to_dict():
    # GIVEN a Card object with known contents
    c1 = Card('something', 'brian', 'todo', 123)

    # WHEN we call to_dict() on the objet
    c2 = c1.to_dict()

    # THEN the result will be a dictionary with known content
    c2_expected = {
        'summary': 'something',
        'owner': 'brian',
        'state': 'todo',
        'id': 123
    }
    assert c2 == c2_expected

class TestEquality:
    def test_equality(self):
        c1 = Card('something', 'brian', 'todo', 123)
        c2 = Card('something', 'brian', 'todo', 123)
        assert c1 == c2

    def test_equality_with_diff_ids(self):
        c1 = Card('something', 'brian', 'todo', 123)
        c2 = Card('something', 'brian', 'todo', 456)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card('something', 'brian', 'todo', 123)
        c2 = Card('something else', 'charlie', 'done', 456)
        assert c1 != c2
