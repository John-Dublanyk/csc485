#CSC485, John Dublanyk
# Example code for the class CSC 485, "Testing for Developers"


## Basic Design

Every homework assignment will involve application code to be tested, and the test code.

The assignment's application code goes in a python package (folder + _ _ init_ _.py file) under the "projects" folder.

The assignment's test code goes in a same-named folder under the "tests" folder.


## Running Code Coverage
In order to run coverage against your project, you need to:
1. install it using ````pip install -U coverage```` from the command line
2. get the version from a ````pip freeze```` command
3. make sure you are in a new local branch!
4. add a line to requirements.txt with the coverage version
5. update your setup.cfg with the following new sections:
````yaml
[coverage:run]
# provide data on branch coverage
branch = True

# ignore the empty __init__.py files
omit = */__init__.py

# just look at the "application" code, not the test code
# this requires that you run your code from your *project* folder
source = suny485/projects

[coverage:report]
exclude_also =
    # don't complain about non-runnable code
    if __name__ == .__main__.:
````

Once code coverage is installed and configured, you can generate your coverage report by running these commands:
````commandline
# use the coverage CLI tool to run pytest
coverage run -m pytest -v --tb=short

# when the tests finish, run the report
coverage report -m

# you should get output that looks like this:

Name                                      Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------------
----------------------------------------------------------
__init__.py                                0      0   100%
projects\__init__.py                       0      0   100%
projects\hw10\__init__.py                  0      0   100%
projects\hw10\fruit_query.py               5      4    20%
projects\hw11\__init__.py                  0      0   100%
projects\hw11\hw11.py                      4      3    25%
projects\hw12\__init__.py                  0      0   100%
projects\hw12\hw12.py                      9      8    11%
projects\hw13\__init__.py                  0      0   100%
projects\hw13\hw13.py                     18     16    11%
projects\hw14\__init__.py                  0      0   100%
projects\hw14\api.py                      12      5    58%
projects\hw14\password_utilities.py       18     16    11%
projects\hw15\__init__.py                  0      0   100%
projects\hw15\api.py                      21     19    10%
tests\__init__.py                          0      0   100%
tests\test_hw10\__init__.py                0      0   100%
tests\test_hw10\test_hw10.py              12      5    58%
tests\test_hw11\__init__.py                0      0   100%
tests\test_hw11\test_hw11.py               6      2    67%
tests\test_hw11\test_hw11_update.py        7      3    57%
tests\test_hw12\__init__.py                0      0   100%
tests\test_hw12\test_hw12.py               6      2    67%
tests\test_hw12\test_hw12b.py              6      2    67%
tests\test_hw12\test_hw12b_update.py       8      3    62%
tests\test_hw13\__init__.py                0      0   100%
tests\test_hw13\test_hw13.py              14     11    21%
tests\test_hw14\__init__.py                0      0   100%
tests\test_hw14\test_api.py               40     29    28%
tests\test_hw14\test_hw14.py              15      9    40%
tests\test_hw15\__init__.py                0      0   100%
tests\test_hw15\test_api_as_code.py       31     29     6%
tests\test_hw15\test_api_as_live.py       32     30     6%
----------------------------------------------------------
TOTAL                                    264    196    26%

````

Documentation on coverage for Python can be found at [Coverage.py](https://coverage.readthedocs.io/en/latest/cmd.html). 
