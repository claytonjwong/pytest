from cards import Card

#
# this helps reduce the redundant code from test_finish.py, but there are problems:
#  1. we have one test case reported instead of three
#  2. if one of the tests fail, we don't know which one without futher debugging the test function
#  3. if one of the tests fail, pytest does NOT run the other tests

def test_finish(cards_db):
    for c in [
        Card('create a course', state='todo'),
        Card('second edition', state='in prog'),
        Card('write a book', state='done')
    ]:
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == 'done'
