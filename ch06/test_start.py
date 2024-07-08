import cards
import pytest
from cards import Card, InvalidCardId

@pytest.fixture(scope="module")
def db_path(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cards_db")
    return db_path


@pytest.fixture()
def cards_db(db_path, monkeypatch):
    monkeypatch.setenv("CARDS_DB_DIR", str(db_path))
    db_ = cards.CardsDB(db_path)
    db_.delete_all()
    yield db_
    db_.close()

@pytest.mark.smoke
def test_start(cards_db):
    i = cards_db.add_card(Card('foo', state='todo'))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == 'in prog'

@pytest.mark.exception
def test_start_non_existent(cards_db):
    with pytest.raises(InvalidCardId):
        cards_db.start(1234567890)
