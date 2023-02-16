# Playwright STX End-to-end tests

## About

The purpose of this repo is to create a structured playground for automating end-to-end tests for the company
page https://www.stxnext.com. Feel free to contribute and have fun!

## Project structure

Project implements Page Object Pattern architecture as it's Playwright compliant and nobody ever got fired for using it.

*

* **Lockfile:** Poetry generates a poetry.lock file that ensures that everyone working on the project uses the same set
  of dependencies with the same versions, which reduces the likelihood of compatibility issues.

* **Packaging:** Poetry makes it easy to package your project for distribution. It generates a pyproject.toml file that
  describes your project and its dependencies, as well as a source distribution and wheel package that you can
  distribute to others.

* **Integration with other tools:** Poetry integrates with other tools, such as Pytest and Flake8, to help you manage
  your project's dependencies and testing.

## Installation

[Poetry](https://python-poetry.org/) is a dependency management and packaging tool for Python that helps you manage your
project's dependencies and
build your project. It's similar to pip, but provides additional features and benefits.

* **Dependency management:** Poetry provides version constraints, installation and updating of packages, and virtual
  environment management.

* **Lockfile:** Poetry generates a poetry.lock file that ensures that everyone working on the project uses the same set
  of dependencies with the same versions

* **Packaging:** Poetry generates a pyproject.toml file that
  describes your project and its dependencies, as well as a source distribution and wheel package that you can
  distribute to others.

* **Integration with other tools:** Poetry integrates with other tools, such as Pytest and Flake8, to help you manage
  your project's dependencies and testing.

### Installation using poetry

#### Installing Poetry

Poetry can be installed via python standard package manager PIP

    pip install poetry

#### Starting environment

To spawn poetry session inside your environment, write

    poetry shell

> This command starts a new shell and activates the virtual environment.
> As such, exit should be used to properly exit the shell and the virtual environment instead of deactivate.

#### Adding dependencies

To add a new dependency to your project, use the add command:

    poetry add <package>

This will add the requests package to your project and update the pyproject.toml file.

#### Installing dependencies

To install dependencies defined in `pyproject.toml`, simply run

    poetry install

### Pre-commit

Pre-commit is a framework used for pre-commits git hooks management. It allows to define actions that confirm that
written code is formatted and configured properly according to defined practices.

**TLDR** you cannot commit stuff unless it's green and your code fits the language guidelines
like [PEP8](https://peps.python.org/pep-0008/)

#### Running pre-commit automatically

To run validation automatically before each commit, please use:

    pre-commit install

This will add pre-commit to git hooks and perform all the checks defined in `.pre-commit-config.yaml`

#### Running pre-commit manually

To check stying in all files, please use

    pre-commit run -a

#### pre-commit in CI

Every pull request should pass pre-commit stage to be merged

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

This repo uses `pytest-xdist` package to allow multiple test being performed in parallel.
Here is an example of running 5 parallel sessions on 3 browsers

    pytest --base-url https://www.stxnext.com -n 5 --browser chromium --browser firefox --browser webkit

#### Artifacts

Playwright comes with video recording and screen capturing out of the box. The results are saved in test-results
directory by default.

    pytest --screenshot={on,off,only-on-failure}

    pytest --video={on,off,retain-on-failure}

## REPL

Sometimes it's convenient to control the browser in interactive session in your python console. To run Playwright
without Pytest, try this snippet

```python
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.stxnext.com")
page.screenshot(path="example.png")
browser.close()
playwright.stop()
```

## GitHub Actions

The purpose of Continuous integration in this repo is to:

1. Validate created Pull Requests - confirm the pre-commit and test are passing
2. Create a template for regularly launched tasks that will Test the targeted environment

## License

[![license](https://img.shields.io/badge/license-MIT-green.svg)](hhttps://github.com/bbrozyna/light-propagation/blob/master/LICENSE)

This project is licensed under the terms of the [MIT license](/LICENSE).
