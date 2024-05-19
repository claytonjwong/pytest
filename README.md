# Python Testing with PyTest

* ISBN-13: 978-1-68050-860-4

## Virtual Environment

### Create Directory for the Virtual Environment

```shell
python3 -m venv venv
```

### Activate the Virtual Environment

```
source venv/bin/activate
```

## Passing Test

*test_one.py*
```python
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
```

### Run Passing Test
```shell
➜  ch01 git:(main) ✗ source venv/bin/activate
(venv) ➜  ch01 git:(main) ✗ pytest test_one.py
============================================================== test session starts ===============================================================
platform darwin -- Python 3.11.5, pytest-8.2.0, pluggy-1.5.0
rootdir: /Users/claytonjwong/sandbox/pytest/ch01
collected 1 item

test_one.py .                                                                                                                              [100%]

=============================================================== 1 passed in 0.00s ================================================================
```

## Failing Test

*test_two.py*
```python
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
```

### Run Failing Test

```shell
(venv) ➜  ch01 git:(main) ✗ pytest test_two.py
============================================================== test session starts ===============================================================
platform darwin -- Python 3.11.5, pytest-8.2.0, pluggy-1.5.0
rootdir: /Users/claytonjwong/sandbox/pytest/ch01
collected 1 item

test_two.py F                                                                                                                              [100%]

==================================================================== FAILURES ====================================================================
__________________________________________________________________ test_failing __________________________________________________________________

    def test_failing():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E
E         At index 0 diff: 1 != 3
E         Use -v to get more diff

test_two.py:2: AssertionError
============================================================ short test summary info =============================================================
FAILED test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
=============================================================== 1 failed in 0.03s ================================================================
```