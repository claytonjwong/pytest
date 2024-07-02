#!/bin/bash

# parametrization techniques are quite effective at creating large numbers of test cases quickly
# as such, it is often beneficial to be able to run a subset of the tests

pytest -v -k todo

# exclude tests with 'create' in their names

pytest -v -k "todo and not create"

# test all parameters for a single function

pytest -v "test_fixture_param.py::test_finish"
