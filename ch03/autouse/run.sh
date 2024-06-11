#!/bin/bash

#
# -s shows the test fixture print messages in the test output
#

pytest -s -v

# (venv) ➜  autouse git:(main) ✗ pytest -s -v
# ================================================================= test session starts ==================================================================
# platform darwin -- Python 3.12.3, pytest-8.2.1, pluggy-1.5.0 -- /Users/claytonjwong/sandbox/pytest/ch02/venv/bin/python3.12
# cachedir: .pytest_cache
# rootdir: /Users/claytonjwong/sandbox/pytest/ch03/autouse
# collected 2 items

# test_autouse.py::test_1 PASSED
# Test duration : 1.0056121349334717

# test_autouse.py::test_2 PASSED
# Test duration : 1.2563419342041016
# --
# Finished : 11 Jun 10:11:09

# ================================================================== 2 passed in 2.27s ===================================================================