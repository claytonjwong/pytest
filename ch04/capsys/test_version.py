import cards
import subprocess

def test_version_v1():
    process = subprocess.run(["cards", "version"], capture_output=True, text=True)
    output = process.stdout.strip()
    assert output == cards.__version__

def test_version_v2(capsys):
    cards.cli.version()
    output = capsys.readouterr().out.strip()
    assert output == cards.__version__

def test_disabled(capsys):
    with capsys.disabled():
        print('\ncapsys disabled print')
