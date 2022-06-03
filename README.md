# Python Automation Framework Template


A Python Automation template with Page Object Model design Pattern

## Tech

This repo used some packages like:

- [Python] - Language used for this framework.
- [Selenium] - Tool for automating web based application.
- [Webdriver Manager] - for handling different webdrivers for testing
- [Pytest] - Unit Testing Framework for Python.
- [DDT] - or Data Driven Testing, a package for handling test data that can be used on test case.
- [softest] - a package that supports assertion and much more.


## Installation

This Project requires [Python](https://nodejs.org/) to run.

Install the packages below by typing on your Terminal
```
pip install selenium
pip install webdriver-manager
pip install pytest
pip install ddt
pip install softest
```

## Run Test Cases
Change the directory to `testcases` folder and type the command below in the terminal
```sh
pytest -vs --browser chrome
```
Note: This Framework only runs on Chrome and Firefox. So change `chrome` to `ff` to run on firefox or vice versa.

[//]: # (links)

   [Python]: <https://www.python.org/>
   [Selenium]: <https://selenium-python.readthedocs.io/>
   [Webdriver Manager]: <https://pypi.org/project/webdriver-manager/>
   [Pytest]: <https://docs.pytest.org/en/7.1.x/>
   [DDT]: <https://www.postgresql.org/>
   [softest]: <https://pypi.org/project/softest/>
