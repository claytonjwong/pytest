import cards
import pathlib
from typer.testing import CliRunner

# the cards app uses a lib called Typer

def test_version_v2(capsys):
    cards.cli.version()
    output = capsys.readouterr().out.strip()
    assert output == cards.__version__

def get_path():
    db_path_env = os.getenv('CARDS_DB_DIR', '')
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / 'cards_db'
    return db_path

def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.strip()

def test_run_cards():
    assert run_cards('version') == cards.__version__

# Like mocking, monkey-patching requires a bit of a mind shift to get everything set up right.
# The function, get_path is an attribute of cards.cli.  We want to replace it with fake_get_path.
# Because get_apth is a callable function, we haev to replace it with another callable function.
# We can't just replace it with tmp_path, which is a pathlib.Path object that is not callable.
def test_path_get_path(monkeypatch, tmp_path):
    def fake_get_path():
        return tmp_path
    monkeypatch.setattr(cards.cli, 'get_path', fake_get_path)
    assert run_cards('config') == str(tmp_path)

def test_path_home(monkeypatch, tmp_path):
    full_cards_dir = tmp_path / 'cards_db'

    def fake_home():
        return tmp_path

    monkeypatch.setattr(cards.cli.pathlib.Path, 'home', fake_home)
    assert run_cards('config') == str(full_cards_dir)

def tes_path_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv('CARDS_DB_DIR', str(tmp_path))
    assert  run_cards('config') == str(tmp_path)
