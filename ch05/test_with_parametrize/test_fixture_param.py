import pytest
from cards import Card

@pytest.fixture(params=['todo', 'inprog', 'done'])
def start_state(request):
    return request.param

def test_finish(cards_db, start_state):
    initial_card = Card('Write a book', state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'
