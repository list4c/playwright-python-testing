# Playwright STX End-to-end tests

## About

## Project structure

## Installation

### Installation using poetry

#### Starting environment

    poetry shell

#### Installing dependencies

    poetry install

### Pre-commit

## Running tests

This project uses `pytest` with `pytest-playwright` as a test runner.

### Defining test choice

#### Running all

To run all the scripts with default setting simply type

    pytest

#### Running specific test

    pytest tests/test_stx_blog.py::test_blog_page_and_filter_articles

#### Running tests matching given expression

    pytest -k stx

For more fancy ways of defining your suite check the official
markers [documentation](https://docs.pytest.org/en/latest/example/markers.html)

### Developer friendly run commands

This will run tests in a headed browser with a delay of 500 milliseconds between actions. It will make observing browser
behaviour easier.

    pytest --headed --slowmo 500

You can insert a breakpoint in your test. It will open interactive pdb session in your console which allows you to use
commands like: [continue, return, quit](https://docs.python.org/3/library/pdb.html#debugger-commands)

```python
def test_something(pytestconfig) -> None:
    base_url = pytestconfig.getini("base_url")
    breakpoint()
```

### Running Tests on Specific Browsers
To run tests on specific browsers, use the Pytest command with the --browser option:

    pytest --browser firefox

This will run tests on Firefox. You can also specify multiple browsers:
    
    pytest --browser firefox --browser chromium


### Other running options

#### Parallel execution
This repo uses pytest-xdist to allow multiple 

    pytest --base-url https://www.stxnext.com -n 5 --browser chromium --browser firefox --browser webkit

## REPL

## Debugging

## GitHub Actions

## Licensing

