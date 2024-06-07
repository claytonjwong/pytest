import cards
from pathlib import Path
import pytest
from tempfile import TemporaryDirectory

#
# with fixture which specifies scope, ie. the fixture will be SETUP once and TEARDOWN once for this module
# instead of SETUP/TEARDOWN for each individual test case
#
@pytest.fixture(scope="module")
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()

def test_empty(cards_db):
    assert cards_db.count() == 0

def test_two(cards_db):
    cards_db.add_card(cards.Card('first'))
    cards_db.add_card(cards.Card('second'))
    assert cards_db.count() == 2
