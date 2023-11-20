#CSC485, John Dublanyk


Example code for the class CSC 485, "Testing for Developers"
Basic Design
=======
# Example code for the class CSC 485, "Testing for Developers"


## Basic Design

Every homework assignment will involve application code to be tested, and the test code.

The assignment's application code goes in a python package (folder + _ _ init_ _.py file) under the "projects" folder.

The assignment's test code goes in a same-named folder under the "tests" folder.

Running Code Coverage
In order to run coverage against your project, you need to:

install it using pip install -U coverage from the command line
get the version from a pip freeze command
make sure you are in a new local branch!
add a line to requirements.txt with the coverage version
update your setup.cfg with the following new sections:
=======

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

Once code coverage is installed and configured, you can generate your coverage report by running these commands:

=======
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


Documentation on coverage for Python can be found at Coverage.py.

## Github Actions, Checks Made on Creating a Pull Request
Github supports workflow actions, instructions to perform various code-related steps and checks when certain things happen. For more info, see [GitHub Actions documentation](https://docs.github.com/en/actions).

We will build instructions to:
1. run our tests when we create a pull request; these tests will run against that pull request's branch, and will exclude tests that require an API server to be running (because  those will fail)
2. generate a coverage report for the tests that were run.


### Setting up our actions
To configure this, we need to have a new directory structure in the project route; this will look like this:
```text
csc485 (project root)
  |- csc485 (package)
  |- .gitignore
  |- requirements.txt
  |- setup.cfg
  |- README.md
  |- pytest.ini
  |- .github      <-- create this folder
    |- workflows  <-- create this folder
      |- push.yml <-- create this file
```

The push.yml file contains the instructions that github will use to configure and launch a docker container and the specific actions to perform on that container:
```yaml
name: Run pytest on PR

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Switch to Current Branch
      run: |
        git checkout ${{ env.BRANCH }}

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m pip install -U pip
        pip install -r requirements.txt
        pip install -e .
        python setup.py install
        echo "[pwd]: ${PWD}"

    - name: Display Troubleshooting Information
      run: |
        echo "[workspace]: ${{ github.workspace }}"
        echo "[pwd]: ${PWD}"
        echo "[LS]: $(ls -al)"

    - name: Run tests and coverage report
      run: |
        # Note: the following commands have three entirely different instances
        # of the "-m" flag. These are positionally required!
        echo "[pwd]: ${PWD}"
        export PYTHONPATH=$PWD/csc485
        echo "[pythonpath]: ${PYTHONPATH}"
        echo "!! run pytest and exclude any live API tests !!"
        coverage run -m pytest -m 'not live_api' --tb=short
        echo "!! run coverage report"
        coverage report -m
```

### Using the actions
You will still create a pull request exactly as you have been doing. Your worklow is:
1. on your local main branch, pull from origin main to get the latest version of code from github.
2. from local main, create a feature branch. This is where you will make your changes.
3. check out your feature branch!
4. write your new code
5. commit your changes
6. push your code to a feature branch on github
7. look at your new branch on github, then click the "create pull request" button
8. Blam! now github runs your action, and you will see status indicator saying that it is in process
9. If you have no syntax errors, the actions will complete and you will get the prompt to rebase your PR. You can choose to review the logs from your actions, which will show your test results and your coverage report.
=======
````

Documentation on coverage for Python can be found at [Coverage.py](https://coverage.readthedocs.io/en/latest/cmd.html). 

