# Python OOP


## Create a virtual env

```shell
python3 -m venv <path_to_name>
deactivate
source <path_to_name>/bin/activate
```

### Install packages in v_env

- Use the following code to install the required modules in the virtual env.
- [requirements.txt](./requirements.txt)
- `python3 -m pip install -r requirements.txt`
- Execute python commands from shell.
    - `python3 -c "import Cars"`

## Packages

- A collection of relatable modules.

### Create a package

- Create a folder with the desired name. Example, Cards.
- Create a python file `__init__.py` and enter the code inside this file.
- The package name is the folder name.

### Application packages

- Two types of packages:
    - Source packages (sdist)
    - Distribution packages (bdist)

- Packaging a python app requires following:
    - Python modules or packages
    - [pyproject.toml file](./packaging/pyproject.toml)
    - A build front-end
    - A build back-end

## Modules

- Standard modules in python; sys, os, math, collections, random, 

- collections.py
    - namedtupes, deque, orderedDict, defaultdict, UserString, ChainMap, COunter, UserDict, UserList

- random.py
    - used to generate random data, but it's a psuedo randomness, better not use in crucial randomness is needed.[]


## Comprehensions

- A shorthand style of syntax that can be replaced for for_loops with a sinngle line of code.
- List, dictionary and Sets.
- [comprehensions.py](./comprehensions.py)


## Exceptions

- Python raises exceptions when there are excpetions to the expected code-flow. There are two main exceptions:
    - Syntax Errors
    - Runtime Exceptions
- Ex: `SyntaxError`, `ValueError`, `FileNotFoundError` etc...
- Exceptions are python objects.
- When there's an error and we can use `raise` keyword to raise and `Exception`.
\
&nbsp;
- Exceptions are raised when the code cannot recover from a situation and don't know how to proceed, we can use exceptions to recover the code and proceed with the flow.
- Can be used for autohealing.
\
&nbsp;
- Can use multiple excaptions in a single try-except block.
- Or can consolidate into a single exception and return a single output.
- In exceptions we can bound a name to the exception raised and use it later in the code.
- Custom exceptions can be created by creating a new class and inheriting the `Exception` class.
- [exceptions.py](./exceptions.py)