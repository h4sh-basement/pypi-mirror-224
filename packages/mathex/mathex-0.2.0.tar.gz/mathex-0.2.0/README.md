# Mathematical Expressions for Python

[![tests status](https://github.com/capsey/mathex-py/actions/workflows/tests.yml/badge.svg)](https://github.com/capsey/mathex-py/actions/workflows/tests.yml)

- [Mathematical Expressions for Python](#mathematical-expressions-for-python)
  - [What is Mathex?](#what-is-mathex)
  - [How to use?](#how-to-use)

## What is Mathex?

Mathematical Expressions (or Mathex for short) is a package for Python that evaluates mathematical expressions from strings at runtime according to [Mathex Specification](https://github.com/capsey/mathex). It aims to provide fast, easy, customizable and, most importantly, safe evaluation with no dependencies.

The package is compatible with Python 3.7+.

## How to use?

Using Mathex is super easy - just import, initialize and evaluate. That's it.

```python
from mathex import Mathex, default_flags

# Use `Config` class and `DefaultFlags` to get default settings.
# For what settings are available, check out documentation.
config = Mathex(default_flags)

# Config class contains your settings along with custom
# variables and functions you inserted.
x = 1.5
config.add_constant("x", x)

# These variables and functions are then available for users
# to use in expressions.
input = "2x + 5"

# Mathex returns error and result of evaluation as a tuple.
result, error = config.evaluate(input)

# If error is None, evaluation completed without errors
if not error:
    print(f"{input} is {result}")  # Outputs `2x + 5 is 8`
```

Don't forget to install Mathex using pip:

```shell
python -m pip install mathex
```
