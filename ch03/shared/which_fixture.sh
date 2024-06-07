#!/bin/bash

#
# if we cannot remember where a particular fixture is located
# then we can use pytest --fixtures -v to provide this info
#
pytest --fixtures -v

# ------------------------------------------------------------ fixtures defined from conftest ------------------------------------------------------------
# cards_db [session scope] -- conftest.py:7
#     no docstring available

# ================================================================ no tests ran in 0.00s =================================================================

#
# we can also filter fixtures used for each test case
#
pytest --fixtures-per-test test_count.py::test_empty

# ------------------------------------------------------------- fixtures used by test_empty --------------------------------------------------------------
# ------------------------------------------------------------------ (test_count.py:4) -------------------------------------------------------------------
# cards_db -- conftest.py:7
#     no docstring available

# ================================================================ no tests ran in 0.00s =================================================================
