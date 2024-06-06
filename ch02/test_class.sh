#!/bin/bash

#
# run all tests within the folder
#
pytest -v

#
# run all tests within a file/module
#
pytest -v test_card.py

#
# run all tests within the TestEquality class
#
pytest -v test_card.py::TestEquality
pytest -v -k TestEquality

#
# run with specific filters, ie. the test name includes 'dict' inclusive-or 'ids'
# and the test name does NOT include 'test_equality'
#
pytest -v -k "(dict or ids) and not (test_equality)"

#
# run a specific test within the TestEquality class
#
pytest -v test_card.py::TestEquality::test_equality

