import pytest
from cards import Card

@pytest.mark.parametrize(
    'start_summary, start_state',
    [
        ('create a course', 'todo'),
        ('second edition', 'in prog'),
        ('write a book', 'done'),
    ],
)
def test_finish(cards_db, start_summary, start_state):
    initial_card = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'
