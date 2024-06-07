#!/bin/bash

#
# tracing fixture execution with --setup-show
#
pytest --setup-show test_count.py

# (venv) ➜  ch03 git:(main) pytest test_count.py --setup-show
# ================================================================= test session starts ==================================================================
# platform darwin -- Python 3.12.2, pytest-8.2.1, pluggy-1.5.0
# rootdir: /Users/claytonjwong/sandbox/pytest/ch03
# collected 2 items

# test_count.py
#         SETUP    F cards_db
#         test_count.py::test_empty (fixtures used: cards_db).
#         TEARDOWN F cards_db
#         SETUP    F cards_db
#         test_count.py::test_two (fixtures used: cards_db).
#         TEARDOWN F cards_db

# ================================================================== 2 passed in 0.02s ===================================================================

#
# tracing fixture execution with --setup-show (with fixture scope="module")
#
pytest --setup-show test_mod_scope.py

# ================================================================= test session starts ==================================================================
# platform darwin -- Python 3.12.2, pytest-8.2.1, pluggy-1.5.0
# rootdir: /Users/claytonjwong/sandbox/pytest/ch03
# collected 2 items

# test_mod_scope.py
#     SETUP    M cards_db
#         test_mod_scope.py::test_empty (fixtures used: cards_db).
#         test_mod_scope.py::test_two (fixtures used: cards_db).
#     TEARDOWN M cards_db

# ================================================================== 2 passed in 0.02s ===================================================================