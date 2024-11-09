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
    - pyproject.toml file
    - A build front-end
    - A build back-end

## Modules

- Standard modules in python; sys, os, math, collections, random, 

- collections.py
    - namedtupes, deque, orderedDict, defaultdict, UserString, ChainMap, COunter, UserDict, UserList

- random.py
    - used to generate random data, but it's a psuedo randomness, better not use in crucial randomness is needed.[]
