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
- In exception handling you can catch multiple exceptions by puting them in a tuple.
    - `except (ValueError, ZeroDivisionError)`
- In exceptions we can bound a name to the exception raised and use it later in the code.
- Custom exceptions can be created by creating a new class and inheriting the `Exception` class.
- [exceptions.py](./exceptions.py)
\
&nbsp;
- Re-raising exceptions, raising more specific exceptions, and exception chaining helps to prevent ineffective handlers.
- It's not always clear how to handle an exception; however they should almost never be uused to silence exceptions.
- If a handler cannot effectively handle the exceptional condition it should be re-raised.
- Exceptions that remain unhandled all the way back through the call stack indicate ineffective or missing handlers.
- Not all exceptions require the original exception to be chained.
- Passing a None value to from keyword causes the original exception to be suppressed.
- [reraise_exceptions.py](./reraise_exceptions.py)
\
&nbsp;
- The class hierarchy for built-in [exceptions](https://docs.python.org/3/library/exceptions.html#exceptions-heirarchy).
- The [BaseException](https://docs.python.org/3/library/exceptions.html#eBaseException).
- Exception handling in 3rd-party applications using heirarchy, [Example](https://github.com/pallets/flask/blob/36af821edf741562cdcb6c60d63f23fa9a1d8776/src/flask/cli.py#L122).


## Classes

- The `self` attribute is bound to the instance of the that class.
- What ever in that first spot will be bound to the the current object from the python runtime.
- Two types of attributes.
    - Class attributes.
    - Instance attributes.
\
&nbsp;
- In a class no need to define the attributes beforehand (class attributes), just put them inside the `__init__` method and it can be used in the other methods. This is called instance attribute defining.
- Instance attributes can be defined inside methods, but better to initialze them when the object was created, these attributes can used as global class attributes.
- `__init__` method is reffered to as a constructor.
\
&nbsp;
- Two types of methods.
    - Class methods: Linked to the type and have access to class attributes and other class methods.
    - Instance methods: Linked to an object instance and have access to both class and instance attributes and methods.


## Inheritance

- The class definition syntax changes when inheriting from other types. Types can be specified inside of parentheses following the class name.

```python
class Shape:
    def __init__(self, area=0):
        self.area = area

class Circle(Shape): ...

class Square(Shape): ...
```


### Single Inheritance

- Inherit from a single base class.
- Base class
    - The class being inheritaed is referred to as a base class.
- Derived class
    - The class inheriting from a base class is referred to as a derived class.
- The Derived class's constructors and methods can be override the methods and constructrs from Inherited class.
- Method overrides can be used to change method signature and/or update/extend methods. 
\
&nbsp;
- `super()` callable has beenfits such as: reduced code duplication, easier code refactoring, etc.
- Base class provide a means of sharing functionality common to multiple derived classes. The Dog class is a derived clas of Animal base class.
- The relationship between base classes and derived classed is commonly referred to as an: is a relationship. For example: a HouseCat an Animal and a Dog is an Animal.
- Derived classes can be used in place of base classes since they inherit all the same attributes. This enables code to be written in a more generic manner.
\
&nbsp;
- The `play_with` function expects a list of Animals both the Dog and HouseCat types can be used. Although derived classes may contain their own unique attributes, the function only uses attributes available to the Animal base class. This enables callables to operate on many different types of objects with shared base classes.
- The derived classes inherit the attribute of the classes which comprise the hierarchy. Terrir and Husky objects inherit the attribute from both the Dog and Animal classes. This allows Terrier and Husky objects to be used in place of either Dog or Animal objects.
- The standard library inclued built-in callables for working with types. The type callable accepts an object and returns its type. Objects include a runtime provided attribute named `__name__` which contains the object's name. The `__name__` attribute reflects the name of named objects and fuctions. The name jojo is bound to a Husky object type which is reflected in the `__name__` binding.
\
&nbsp;
- The built-in `issubclass` callable is used to determine if one type is a subclass of another. The term subclass indicates that a type is derived from another class at some point in the heirarchy.
- the built-in `isinstance` callable is used to determine if an instance has a specific type. The isinstance callable returns True if the type of the provided object instance inherits one of the specified types at some point in the heirarchy. The isinstance callble accepts an object instance and a type or tuple of types.
