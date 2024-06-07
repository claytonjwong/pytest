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