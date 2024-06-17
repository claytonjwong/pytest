#
# To help understand the problem parametrized testing is trying to solve, let's write some tests for the finish() API:
#

# def finish(self, card_id: int):
#     """set a card state to 'done'"""
#     self.update_card(card_id, Card(state="done"))

from cards import Card

def test_finish_from_todo(cards_db):
    index = cards_db.add_card(Card('create a course', state='todo'))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'

def test_finish_from_in_prog(cards_db):
    index = cards_db.add_card(Card('second edition', state='in prog'))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'

def test_finish_from_done(cards_db):
    index = cards_db.add_card(Card('write a book', state='in prog'))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'
