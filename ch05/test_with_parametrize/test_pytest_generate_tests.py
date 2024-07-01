import pytest
from cards import Card

def pytest_generate_tests(metafunc):
    if 'start_state' in metafunc.fixturenames:
        metafunc.parametrize('start_state', ['todo', 'inprog', 'done'])

def test_finish(cards_db, start_state):
    initial_card = Card('Write a book', state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'
