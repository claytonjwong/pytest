#!/bin/bash

pytest --setup-show

# (venv) ➜  multiple_fixtures git:(main) ✗ pytest --setup-show
# ================================================================= test session starts ==================================================================
# platform darwin -- Python 3.12.3, pytest-8.2.1, pluggy-1.5.0
# rootdir: /Users/claytonjwong/sandbox/pytest/ch03/multiple_fixtures
# collected 3 items

# test_count.py
# SETUP    S db
#         SETUP    F cards_db (fixtures used: db)
#         test_count.py::test_empty (fixtures used: cards_db, db).
#         TEARDOWN F cards_db
#         SETUP    F cards_db (fixtures used: db)
#         test_count.py::test_two (fixtures used: cards_db, db).
#         TEARDOWN F cards_db
#         SETUP    F cards_db (fixtures used: db)
#         test_count.py::test_three (fixtures used: cards_db, db).
#         TEARDOWN F cards_db
# TEARDOWN S db

# ================================================================== 3 passed in 0.00s ===================================================================

pytest --func-db --setup-show

# (venv) ➜  multiple_fixtures git:(main) ✗ pytest --func-db --setup-show
# fixture_name: db
# ================================================================= test session starts ==================================================================
# platform darwin -- Python 3.12.3, pytest-8.2.1, pluggy-1.5.0
# rootdir: /Users/claytonjwong/sandbox/pytest/ch03/multiple_fixtures
# collected 3 items

# test_count.py
#         SETUP    F db
#         SETUP    F cards_db (fixtures used: db)
#         test_count.py::test_empty (fixtures used: cards_db, db).
#         TEARDOWN F cards_db
#         TEARDOWN F db
#         SETUP    F db
#         SETUP    F cards_db (fixtures used: db)
#         test_count.py::test_two (fixtures used: cards_db, db).
#         TEARDOWN F cards_db
#         TEARDOWN F db
#         SETUP    F db
#         SETUP    F cards_db (fixtures used: db)
#         test_count.py::test_three (fixtures used: cards_db, db).
#         TEARDOWN F cards_db
#         TEARDOWN F db

# ================================================================== 3 passed in 0.01s ===================================================================
