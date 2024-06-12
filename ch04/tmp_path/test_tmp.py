def test_tmp_path(tmp_path):
    file = tmp_path / 'file.txt'
    text = 'hello world'
    file.write_text(text)
    assert file.read_text() == text

def test_tmp_path_factory(tmp_path_factory):
    path = tmp_path_factory.mktemp('something')
    file = path / 'file.txt'
    text = 'hello world'
    file.write_text(text)
    assert file.read_text() == text
