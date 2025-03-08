# Python OOP


## Create a virtual env

```shell
python3 -m venv <path_to_name>
deactivate
# activate the virtual env
source <path_to_name>/bin/activate
python3 -m pip install --upgrade pip
```

```shell
# remove all third-party modules from the v_env by re-creating it
deactivate
python3 -m venv <path_to_name> --prompt="display_name" --clear
# activate the virtual env
source <path_to_name>/bin/activate
python3 -m pip install -U pip
```

### Install packages in v_env

- Use the following code to install the required modules in the virtual env.
- `python3 -m pip install --upgrade pip` can use `> /dev/null` to nullify the
- [requirements.txt](./requirements.txt)
- `python3 -m pip install -r requirements.txt`
- Execute python commands from shell.
    - `python3 -c "import Cars"`

> [!CAUTION]
> To delete the v_env `python3 -d <path_to_name>`

## Packages

- A collection of relatable modules.


### Regular package vs Namespace package

- If a directory contains `__init__.py` the Python treats it as a __regular__ package.
- If there are sub packages and modules spread across multiple directories and they don't have the dunder file in it Python treats them as __namespace__ packages.

> - root_dir/
>   -   ├── employee_sales/
>       -   ├── department/
>           -   ├── sales/
>               -   ├── `__init__.py`
>               -   └── `analytics.py`
>       -   ├── sample/
>       -   ├── .../
>   -   ├── employee_hr/
>      -    ├── department/
>           -   ├── hr/
>               -   ├── `__init__.py`
>               -   └── `policies.py`
>      -    ├── sample/
>      -    ├── .../

- What happens is that when python search through the project directory; as an example import sample, first it searches for a regular package.
- If it couldn't find a regular package but finds a `sample.py` it imports as a module.
- If neither of them were found but instead finds 1 or more directories named sample it creates a namespace package by combining the folders.

```shell
# if a regular package or a module is found it'll be stopped at this first line
>>> from this import sample
# if namespaces were created
>>> sample.__path__
>>>['root_dir/employee_sales/sample', 'root_dir/employee_hr/sample']
```


### Application packages

- Two types of packages:
    - Source packages (sdist)
    - Distribution packages (bdist)

- Packaging a python app requires following:
    - Python modules or packages
    - [pyproject.toml file](./packaging/pyproject.toml)
    - A build front-end
    - A build back-end


## Python Dependency Managemnt with Pip

### PIP and Python Package Index (PyPI)

- Python package index is a repository of python code.
- Manages 1000s of modules created by python devs around the world.
- In context of Package index: package refers to a distribution package.
- [Pypi.org](https://www.pypi.org) is the package page & pip is the tool used to install (package installer for python).
- The repo consist of,
    - Text-based templates
    - NLP libraries
    - Web Application Servers
    - Video Game Engines

> [!NOTE]
> This code/module is considered as *untrusted code*.
> Such code should be reviewed carefully before applying to your application.


### Package Versions

- Python runtime includes a dir `python/lib/python<version>/site-packages` which is used to store/install the third-party modules/packages.
- External code changes can affect your code in significant ways due to package versions.
- multiple apps can require different versions of the same package which could lead to version conflicts.
- Pip provides a mechanism for installing specific versions of a package.
- Virtual environments (venv) module provides a support for creating light weight venvs with their own site-directories isolated from the system site-directory.


### Package Selection

- There are few considerations to be done before selecting a package from the package repo.
    1. Licensing - Does the package's license allow you to use the code as needed?
    2. Documentations - Does the package contain useful documentation?
    3. Effort Savings - Does the introduction of this package save enough effort to justify using it?
    4. Quality - Does the package contain test that validate the code? Is the code close enough to be considered idiomatic?
    5. Security - Does the package take reasonable considerations to maintain security?
- These are just few topics to consider and there can be other topics to consider. More the better.


### Package Install

- Package Installer for Python (pip) is the tool for installing packages for python.
- `python3 -m pip` gives the available commands with pip.
    - `list` gives the installed packages and other dependecies with version.
    - `install <package>` will locate, download and install a package.
    - `install <package>==<version>` to install a specific version of a package.
    - `uninstall <package>` will uninstall the package.
    - `-y` will auto configure the Yes for the prompt.
    - guide for [pip](https://pip.pypa.io/en/stable/cli/pip_install/)

| SYMBOL | OPERATOR NAME | DESCRIPTION |
| --- | ---- | ---- |
| == | Matching operator | For an exact match |
| != | Exclusion operator | To exclude a version |
| <> | Exclusive order operator | To include versions of greater or lesser versions |
| <= >= | Inclusive order operator | To include versions of greater or equal or lesser or equal value |
| ~= | Compatible version operator | Used as a shorthand syntax that compresses multiple version specifiers |
| === | Arbitrary Matching operator | Used to match exact strings; Also provides a mechanism for matching the text of the version for packages that don't follow the expected version structure |

- Example: `python3 -m pip install "rich==12.4.*, < 12.4.4"`


### Manage Package Versions

- Community standard is to maintain the required packages for an application in an text file named `requirements.txt`
- A typical [requirements.txt](requirements.txt) file.
- `python3 -m pip install -r requirements.txt` will install the packages and the exact versions specified in the text file.
- `pip freeze` is a way to list the current installed package version specifiers. Can be used to create a backup if we are trying to upgrade any packages and dependencies.
- After testing with any latest version upgrades and need to revert back to the previous versions we can run the command to install the packages from the requirements file, it will remove the latest versions and install the required versions.
- If there are multiple requirements files and depending on the application type can categorize the requirements. If a requirement file need to install dependencies from another can add a command line argument to be passed to pip install.
- Add the following line in the prod_requirement.txt if need to install dependencies from the dev file `-r dev_requirement.txt`


### Manage Packages for Multiple Projects (venv)

- `venv` module is used to create isolated python environments, named virtual environment.
- `python3 -m venv <path_to_dir>` is used to create the env.
- `source <path_to_dir>/bin/activate` is used to initialize the env. `deactivate` is used to deactivate the current active virtual environment.
- This is activated only in the current active terminal and for multiple terminals we can have different vir_envs activated.
- This env is created with the current available python runtime hence it's similar to the current available python version and it's better to create new vir_envs for new python versions.


### Name-based and URL-based

- There are two ways to install packages,
    - Name-based: can be installed by refering to the python package name if it's available in the pypi repo.
    - URL-based: can be installed by specifying the exact git url of the package from the source code.
    - `python3 -m pip install "rich @ git+https://github.com/Textualize/rich.git"`
    - Better to use `python3 -m pip install git+https://github.com/Textualize/rich.git@main`

> [!NOTE]
> The package name and URL are seperated by an `@` symbol.


### Environment Markers

- Environment markers are used to determine is a dependency is required for the given runtime env.

| Marker | Code Equivalent |
| ---- | ---- |
| os_name | os.name |
| sys_platform | sys.platform |
| platform_machine | platform.machine() |
| platform_python_implementation | platform.python_implementation() |
| platform_release | platform.release() |
| platform_system | platform.system() |
| platform_version | platform.version() |
| python_version | `'.'.join(platform.python_version_tuple()[:2])` |
| python_full_version | platform.python_version() |
| implementation_name | sys.implementation.name |

- Example: `python3 -m pip install "rich, python_version>'3.8' and sys_platform=='linux'"`

> [!NOTE]
> The **darwin** platform represents macOS.
> `python3 -m pip install "rich, python_version>'3.8' and sys_platform=='darwin'"`

- Install an extra dependency of rich.
    - `python3 -m pip install rich[jupyter]`

- Example: `python3 -m pip install "rich[jupyter] @ git+https://github.com/Textualize/rich.git@v12.3.0 ; python_version>'3.8' and sys_platform=='linux'"`


### Create a package

- Create a folder with the desired name. Example, Cards.
- Create a python file `__init__.py` and enter the code inside this file.
- The package name is the folder name.
- Packaging [guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

```shell
# upgrade the pip
python3 -m pip install --upgrade pip
# go to the directory and create the pyproject.toml
# configure metdata
touch pyproject.toml
# create README.md
touch README.md
# include other files for distibution

# generate distribution archives
python3 -m build
```

> - dist/
>   - ├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
>   - └── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz

- The `tar.gz` file is a *source distribution* whereas the `.whl` file is a *built distribution*.
- Newer pip versions preferentially install built distributions, but will fall back to source distributions if needed.
- You should always upload a source distribution and provide built distributions for the platforms your project is compatible with.


## Point of Interest - Poetry

- Dependency management can become a challenge. Especially regarding the creation and distribution of packages. Pip makes it easy to download and install dependent modules. However, the Python ecosystem doesn't make creating and distributing packages as simple as it could.
- The open source [**Poetry**](https://python-poetry.org) module attempts to simplify this process. [Poetry](https://github.com/python-poetry/poetry) replaces much of the boiler plate code and configuration around packaging with a single *pyproject.toml* file.

- Example: [pyproject.toml](./packaging/poetry_pyproject.toml)


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


### Multiple Inheritance

- Single inheritance represents a chain of base classes. The runtike searches for methods in a specific order. First the current class is checked before working up through the heirarchy all the way up to the root object base class. The conceptual simplicity of single inheritance makes it relatively intuitive to understand.
- Multiple inheritance is a far less straightforward concept which requires careful design to avoid common pitfalls. Many programming languages/runtimes are intentionally limited to single inheritance to avoid the potential complexity. Multiple base classes might include implementations of the same method.
\
&nbsp;
- Both B and C are derived from class A. Class D is derived from both B and C.
- When the run method is called for an instance of class D which implementation of run should be called?
- This is commonly referred to as the Diamond problem
- `D().run()` Notice that the runtime called the method from the class C.
- `E().run()` the runtime called the method from the class B.
- The runtime includes logic to determine the order that base classes are checked for a requested method. This is referred to as the *method resolutio order* (**mro**).
- Every object type includes a list of base classes representing the method resolution order.
- The runtime inclused mechanisms used to determine the resolution order. Object types include a class method named `mro` and a class attribute named `__mro__`.
- The mro method returns a list of base classed in resolution order. The `__mro__` attribute includes the same information as a tuple.
\
&nbsp;
- Notice the mro, the runtime first checks for methods on the calling class before moving through the other classes. The runtime uses the C3 linearization algorithm.

> [!IMPORTANT]
> Guido van Rossum the creater of Python describes C3 thusly:
> Basically, the idea behind C3 is that if you write down all of the ordering rules imposed by inheritance relationships in a complex class hierarchy, the algorithm will determine a monotonic ordering of the classes that satisfies all of them. If such an ordering can not be determined, the algorithm will fail.

- Below is a summary of how it imapcts the mro.
 
    - Derived classes are checked before base classes.
    - Classes inheriting from multiple base classes maintain the base class order specified in the class defintion.
    - Class are never repeasted.
    - Replace the class definition dor A with the following code.

`[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]`
- Notice that the A class is only specified once even though both B and C inherit from the A class.
\
&nbsp;
- Multiple inheritance is omitted in many other programming languages/runtimes due to the potential method resolution ambiguity. Effective multiple inheritance requires careful ddesign in order to avoid tangled object heirarchies that are difficult to maintain. Two common use cases for mutiple inheritance include method delegation and mixins.


### Method delegation

- Method delegation can assist with the diamond problem by delegating method calls to base classes. The built-in super callable used with single inheritance returns the base class. When used with multiple inheritance the super callable demonstrates its true power.
- Consider the following goal: create a dictionalry that normalizes keys as lowercase alphanumeric characters. this can be easily accomplished by useing the built-in dict type as a base class.
- The NormalizedDict class overrides the `__setitem__` and `__getitem__` magic methods and delegates to the base class.

> [!NOTE]
> New to magic methods? Learn how to make objects behave nore like built-in objects using magic methods.

- The NormalizedDict uses single inheritance to take on the behoaviours of the built-in dictionary. Inside the `__setitem__` method the `normalize_key` function normalizes the key to lowercase alphanumeric characters. Calling `super().__setitem__` delegates responsibility to the `dict.__setitem__` method. The `__getitem__` method also delegates responsibility to the base class method of the same name.
- `print(scores)` notice how the keys reflected are in lowercase alphanumeric characters.
\
&nbsp;
- Both the NomalizedDict and AdjustedValueDict classes inherit from the built-in dict class and delegate the overriden calls to the base class.
- The PlayerScoreDict uses multiple inheritance to combine three base classes: `NormalizedDict`, `AdjustedValueDict` and `collections.defaultdict`.
- Each class inheirts from the dict class.
-  `print(scores)` notice that the keys are normalized from the `NormalizedDict` class. The Values are adjusted by a factor of 1_000 from the `AdjustedValueDict` class. The `defaultdict` ensures that using the dictionary lookup syntax for the key 'MISSING' returns a default value rather than raising an exception.
- The `PlayerScoreDict` class takes ib tge functionality from each base class. This is possible due to using super for method delegation.

`[<class '__main__.PlayerScoreDict'>, <class '__main__.NormalizedDict'>, <class '__main__.AdjustedValueDict'>, <class 'collections.defaultdict'>, <class 'dict'>, <class 'object'>]`
- Each base class has the same parentage, the mro matches the order that base classes are defined. Each base class delegates it's calls to its base class. **This ensures that the functionality of each base class is applied before delegating to the next base class**.
- Using multiple inheritance as a method delegation mechanism can produce more maintainable and reusable code. This design style requires careful consideration for method signatures. Derived classes must be able to provide the required arguments to multiple base classes.


### Mixins

- Mixins are another common use case for multiple inheritance in Python. Mixins are not intended to be instantiated and used directly. They're used to provide required functionality to derived classes.
- For example, an authentication mixin might add user authentication functionality to classes used for handling web requests.
- In the `AuthMixin` class `self.header` in the `is_authenticated` method, this attribute is not defined as part of the `AuthMixin` class. Mixin classes enhance derived classes and are not intended to be used as standalone classes. The `AuthMixin` class requires that derived classes include a header attribute.
- The `JSONMixin` class is used to convert JSON data into Python objects if the reuest type is `application/json`.
- The `Request` class inherits from both mixin classes. The process method uses mixin methods to perform authentication and deserialization.

> [!IMPORTANT]
> Carefully designed mixins can prevent the risk of ambiguous method resolution by providing a limited number of very specific methods.


### Abstract Base Classes

- Not all base classes provide their own implementations. SOme base classes are intended to serve as interfaces for developers to override. This type of base class is referred to as an abstract base class.
- Abstract base classes define an interface that derived classes must implement.

> [!WARNING]
> `TypeError: Can't instantiate abstract class Text with abstract method render`

- The derived class must implement the interface in the abstract base class.
- The standard library includes a module named abc used for creating abstract base classes.
- The `Renderable` class derives from the ABC (Abstract BaseClass) type and uses the abstract method decorator to mark the render method as abstract.
- The `Renderable` class cannot be directly instantiated. It must be derived and its abstract methods must be implemented.
- It ensures that classes with `Renderable` in the base class hierarchy msut be implement the render method.


### Composition

- Object inheritance is a core aspect of oop. It's used inside the Python runtime by every object execpt for the root type named object. Object composition is another aspect of object oriented programming. Composition consists of accessing the functionality from other object types through attributes. Where inherited objects have an is a relationship, composite object are more of a has a relationship.
- Composition consists of interacting with other object types through attributes. Composite classes leverage the functionality of the classes without augmentation. Unlike inherited classes which allow derived classes to augment the functionality of the base class.
- The code in [composite_classes.py](composite_classes.py) demonstrates composition by modeling a rudimentary company. The mode is composed of the following classes: `Employee`, `Department`, and `Company`. The `Company` class is composed from the other two classes.
- The `Employee` class is composed of the built-in str type and itself. The `manager` attribute is a reference to another instance of `Employee`.

`C suite: [Q Q, R R, S S] Departments: [HR: headed by: Y Y. Team: [A A, B B], DEV: headed by: Z Z. Team: [C C, D D]]`


## Summary on Classes

- OOP consists of bundling data and code together into a single entity referred to as an object. Objects are the atomic building block of the python runtime. Object inheritance is a core aspect of oop. Inheritance allows classes to derive behaviors from other classes to form object hierarchies.
- All objects inside of the Python runtime inherit from the built-in object type at the top of the hierarchy. the object type contains attributes that are common to all other types. Python supports both single and multiple inheirtance. Single inheritance forms a chain of derived/base classes where each object inherits from a single base class. Multiple inheirtance allows derived classes to inherit from mutiple base classes.
- Multiple inheirtance introduces complexity in the form of potentially ambiguous mro and maintenance challenges. Careful design considerations are required with mutiple inheritance to avoid these common pitfalls. multiple inheritance is commonly used for mixins and method delegation.
- Mixins are base classes which are not intended to be instantiated directly. they're used to provide commonly required functionality to derived classes. Commonly web applocation frameworks leverage mixins to provide functionality such as authentication inside the context of a web request.
- Method delegation leverages the built-in super callable to delegate calls to the next base class in the method resolution hierarchy. Using multiple imheirtance for delegation requires knowledge of the base classes. Derived classes inheirting from the same base class can be chained together through method delegation. Effective method delegation requires careful consideration for method signatures.
- Base classes without default implementations can be created using abstract base classes. Inheirting from the abs.ABC class turns a derived class into an abstract base class. The abc.abstractmethod decorator allows methods to be marked as abstract. Abstract methods must be implemented by derived classes or else an exception is raised.
- Composition consists of interacting with other object types through attributes. Composite classes leverage the functionality of other classes without augmentation. Unlike inherited classes which allow derived classes to augment the functionality of the base class.
- Objects are useful mechanisms for modeling real world and abstract concepts (people, places, things, text, numbers, etc...). However, not everything needs to be modeled using classes. Functions are commonly more than sufficient for a given task.

[dev_conf.json](dev_conf.json)
[dev_conf.py](dev_conf.py)

- Both implementations produce the same output however, the function-based approach is more simple implementation. Simple code reduces the surface area for bugs to hide as well as maintenance burdens.


## Magic Methods

> [!NOTE]
> Defined in the `__init__.py` is a function named display that prints two values separated by tabs. The display function is used in here to show a Python expression on the left and the expression's result on the right.


> [!TIP]
> Need to run the following command from the parent folder `pythons -m oop.magic_methods`

### Introduction

- Objects interact with the Python language syntax and runtime in different ways.

```py
# Operators
a = 100 > 42
b = 40 + 2

# Checking and object's truthiness
scores = [100, 64, 85, 39, 74]
if scores:
    sum(scores)

# Using an object as a context manager
with open('file', 'w') as f:
    f.write('hey')

# Converting object types
amount = float(input('Enter an amount to wager >'))
```



- Python objects include specially named methods that allow control over these types of interactions. These are commonly referred to as magic methods of dunder methods.
- Most common magic ( dunder ) method is `__init__`. This constructor is responsible for performing object initialization. the `__init__` method is called by the runtime when an object is created.
- Some magic methods such as `__init__` allow for developer defined method parameters. Others such as `__str__` method must use a fixed method signature.


### Magic Methods

- The `display` outputs a ruintime specific string representation. This default representations displays the module and class name followed by the object's memory address.
- The `__str__` method is used to convert an object into a str representation when passed to the built-in str, print, and format callables.
- Implementing the `__str__` method is useful when working with objects that have a natural str representations.

```shell
# before __str__
str(account_a)          <__main__.Account object at 0x7fa306ff8dc0>
str(account_b)          <__main__.Account object at 0x7fa3070b3820>

# after __str__
str(account_a)          account: savings balance: 200.42
str(account_b)          account: checking balance: 400.42
```

- The `__str__` method is also useful for debugging using the built-in print callable.
- The `__int__` and `__float__` methods are used to convert objects into int and float types.
- The `__repr__` method is similar to the `__str__` method except that `__repr__` is intended for developers. The `__repr__` method commonly displays a string representing the code required to recreate the object. Passing an object to the built-in `repr` function calls the objects `__repr__` method.
- The `__repr__` is called by other built-in callables, print and format may call `__repr__` method as a fallback if no `__str__` method exists.
\
&nbsp;
- Comparison methods allow objects to be compared using operators.
- The `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__` methods in this example [magic_methods.py](magic_methods.py) uses numeric comparisons and are not limited to numeric comparisons, these methods are intended to allow objects to be compared in a natural manner.
- The class `Player` is an example implementation of the equality method to compare str values.

```py
class Player:
    def __init__(self, handle):
        self.handle = handle

    def __eq__(self, other):
        return self.handle == other.handle
    
p_a: Player = Player('smasher')
p_b: Player = Player('crasher')
p_c: Player = Player('smasher')

assert p_a == p_c
assert p_a != p_b
```


> [!NOTE]
> The assert statement has two main uses:
> > 1. It helps detect problems early in the program, where the cause is clear, rather than later when some other operation fails.
> > 2. Works as a documentation for other developers.
> As references [Simple statements](https://docs.python.org/3/reference/simple_stmts.html) & [Assertion in Python](https://pythongeeks.org/assertion-in-python/)

```py
assert condition
# the above can be written as below
if not condition:
    raise AssertionError()
```


### Truthiness

- Objects in Python process a quality called truthiness that determines if the object represents a bool value of *True* or *False*.
- It is determined by one of two possible methods: `__bool__` or `__len__`. If the `__bool__` method is implemented the runtime uses it to determine truthiness. The `__len__` method is used as a fallback. 
- All built-in object types include truthiness logic. Numeric zero values and empty sequences evaluate as *False*
- Example code can be found in [truthiness.py](truthiness.py)

> [!NOTE]
> User-defined objects omitting both magic methods evaluate as True.

- Truthiness of built-in types:
```py
assert not None
assert not bool(0)
assert bool(1)
assert bool(-1)
assert not bool('')
assert not bool([])
assert bool([1])
assert not bool({})
assert bool({0:0})
assert not bool(set())
assert bool(set([1]))
assert not bool(range(0))
assert bool(range(1))
```


- The `__len__` method is determines the length of an object via the built-in len callable. the `__len__` method is expected to return an *int* value greater than or equal to zero.
- This method is used as a fallback for determining truthiness if the `__bool__` method is not implemented. A value of zero evaluates as *False* otherwise *True*.
\
&nbsp;
- Initially since none of the methods are implemented in the `Accounts` class, it evaluates as *True*. 
```shell
accs is True
```
- After the `__len__` method is implemented, it evaluates as *False*.
```shell
Called the __len__ method.
accs is False
```
- The `Account` objects in the `Accounts` constructor will be evaluted as *True* now that accounts exists in the list.
- The `__len__` method works best for objects with a natural representation of length, and works well with sequences. May not work for all objects.
\
&nbsp;
- The `__bool__` method provides more precise control over an object's truthiness.
- The below returns only if the account object has the attribute active set as True

```py
any(a for a in self.accs if a.active)
```

- With the above implementation, now it evaluates as *False*, and making one account *active*=**True** evaluates as True.
```shell
Primary Secondary
Called the __bool__ method.
accs is True
Called the __len__ method.
accs contains 2 accounts
```

> [!NOTE]
> Having finite control over an object's truthiness reduces the amount of code required to perform boolean operations.

- Truthiness also allows conditional name bindings using the *or* operator.
- In the below example the `name` keyword defaults to `None` which evaluates as *False*. The line `name = name or 'Human'` instructs the runtime to assign the name binding to itself if it evaluates as *True* otherwise use the value following the *or* operator.

```py
def some_function(name=None) -> None:
    name = name or 'Human'

# the same can be written as (the longhand syntax)

def some_function(name=None) -> None:
    if name is None:
        name = 'Human'
```

- An aside on boolean expressions Developers commonly perform boolean comparisons using code similar to the following:

```py
if some_object == True:
    do_something()
```

- Directly comparing an object to *True* is overly verbose and unnecessary. It can be consolidated to:

```py
if some_object:
    do_something()
```


## Summary on Magic Methods

- Magic methods should be used to allow user-defined objects to behanve more like built-in objects. They allow objects to interact with the runtime and language syntax in a more Pythonic manner. A wide range of methods exist for performing actions such as overriding operators.


## Challenge Sparkle & Shine

- `@property`: Properties in python are typically used for attributes that need to be computed or processed everytime they are accessed, and they should not take arguments other than `self`. The `activate` method was intended to be a regular method that can take an `amplifier_callable` argument, so making it a property is incorrect.
- The `Sparkle` and `Shine` classes had default parameters in their constructors, which weren't necessary. These classes are meant to initialize with fixed points and avatars, so simplifying them by directly passing these values to the base class `Power` makes the code cleaner and easier to understand.
- The original `activate` method of `SuperSlothBot` had some logical issues, including improperly setting `self.last_power` and not handling out-of-range numbers correctly.
    - It raises a `ValueError` if the number is not between 0 and 50.
    - It correctly assigns a `Sparkle` or `Shine` object to `self.last_power` based on the number's range.
    - It calls the `activate` method of the appropriate `Power` object.
- The `__str__` method originally could crash if `self.last_power` was not set because it would try to access `avatar` and `points` attributes that didn't exist. Adding a try-except block with `AttributeError` ensures the method returns a fallback message if `self.last_power` is `None`.


## Class and Objects Practice Challenges: Beginer Level

- [Library Management System](challenge_libraryms.py)
    - Create a class structure for a simple library management system. The system should allow adding new books, borrowing books, and returning books.
    - Try to pass the `title` of the book as a string.
    - Add a book search method to look up for books by title using list comprehension.
```py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Implement the logic to add a book to the library

    def borrow_book(self, title):
        # Implement the logic to borrow a book from the library

    def return_book(self, title):
        # Implement the logic to return a book to the library

# Example Usage
library = Library()
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

# Try borrowing and returning books
```

- [E-Commerce Order Processing](challenge_ecommop.py)
    - Create a class structure to represent an order processing system for an e-commerce website. The system should manage products, orders, and customers.
    - Original implementation is okay, used type annotations for the method parameters and return types for consistency.
    - Dict for items: If the same item was added multiple times might need to consider how to handle that.
    - Edge cases: items without a quantity was added.
    - String represntation: `__str__` & `__repr__` methods for readbility and debugging.
```py
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        # Implement the logic to add an item to the order

    def get_total(self):
        # Implement the logic to calculate the total cost of the order

# Example Usage
customer = Customer("John Doe", "john@example.com")
order = Order(customer)

product1 = Product("Laptop", 999.99)
product2 = Product("Mouse", 49.99)

order.add_item(product1, 1)
order.add_item(product2, 2)

total = order.get_total()
```

- Property Decorator: The `get_total` method is now decorated with `@property`, so it can be accessed as an attribute (`order.total`).
- Consistency and Readability: Using properties can make the code more readable and consistent with how other attributes are accessed.
\
&nbsp;
- [School Management System](challenge_schoolms.py)
    - Create a class structure to represent a school management system. The system should manage students, teachers, and courses.
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        # Implement the logic to add a student to the course

# Example Usage
teacher = Teacher("Mr. Smith", 40, "Mathematics")
course = Course("Algebra 101", teacher)

student1 = Student("Alice", 16, "S123")
student2 = Student("Bob", 17, "S124")

course.add_student(student1)
course.add_student(student2)
```


## Class and Objects Practice Challenges: Intermediate Level

- More challenges with a bit of extended implementations.
- [Banking System](challenge_banking.py)
    - Create a class structure for a simple banking system. The system should manage customers, accounts, and transactions. Implement functionality for depositing, withdrawing, and transferring funds between accounts.
```py
class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f'Customer(name={self.name}, email={self.email})'

class Account:
    def __init__(self, customer: Customer, account_number: str) -> None:
        self.customer = customer
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        # Implement the logic to deposit funds

    def withdraw(self, amount: float) -> None:
        # Implement the logic to withdraw funds

    def transfer(self, amount: float, target_account) -> None:
        # Implement the logic to transfer funds to another account

    def __str__(self) -> str:
        return f'Account(account_number={self.account_number}, balance={self.balance})'

# Example Usage
def test_example() -> None:
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    account1 = Account(customer1, "12345")
    account2 = Account(customer2, "67890")

    account1.deposit(1000)
    account1.transfer(200, account2)
    account1.withdraw(100)

    print(account1)
    print(account2)

if __name__ == '__main__':
    test_example()

```

- The implementation is great; Optimizing tips to consider.
- When Type annotation is done for the same Class type within the class itself need to put it within quotes. [Forward References](#forward-references-in-class)
- When naming methods `balance_not_sufficient` should be `is_balance_insufficient` for clarity.
- Avoid redundency: The else statement is redundant after return statements.
```py
if amount <= 0:
    print(f'Withdrawal amount should be greater than Zero')
    return
elif self.is_balance_insufficient(amount):
    print(f'Remaining balance is not sufficient to withdraw.')
    return
else:
    self.balance -= amount
    print(f'Successfully withdrawed an amount of {amount}, available balance is {self.balance}.')
    return

# should be

if amount <= 0:
    print('Withdrawal amount should be greater than zero.') 
    return
if self.is_balance_insufficient(amount): 
    print('Insufficient balance for withdrawal.') 
    return 
self.balance -= amount
print(f'Successfully withdrew {amount}. Available balance is {self.balance}.')

```
- Edge cases should be handled correctly; When transferring check if the target account is the same as source account.


\
&nbsp;
\
&nbsp;
\
&nbsp;
- [Library Management System (Extended)](challenge_ext_libraryms.py)
    - Extend the previous library management system to include a system for managing library members, book reservations, and late fees.
    - The original code is correct, for improvements;
    - Ensure error handling.
    - Use set or dict structures for lookup efficiency.
    - Try to borrow the book if the book is available and no need to wait.
    - `from typing import List` to specify the type of the books and members attributes in the `Library` class. This makes the code more readable and helps with type checking, making it clear that these attributes are expected to be lists of `Book` and `Member` objects, respectively.
```py
class Member:
    def __init__(self, name: str, member_id: str) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book) -> None:
        # Implement the logic to borrow a book

    def return_book(self, book) -> None:
        # Implement the logic to return a book

    def __str__(self) -> str:
        return f'Member(name={self.name}, member_id={self.member_id})'

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self) -> str:
        return f'Book(title={self.title}, author={self.author})'

class Library:
    def __init__(self) -> None:
        self.books = []
        self.members = []

    def add_book(self, book: Book) -> None:
        # Implement the logic to add a book to the library

    def register_member(self, member: Member) -> None:
        # Implement the logic to register a member

    def reserve_book(self, book: Book, member: Member) -> None:
        # Implement the logic to reserve a book

    def __str__(self) -> str:
        return f'Library(books={len(self.books)}, members={len(self.members)})'

# Example Usage
def test_example() -> None:
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    member1 = Member("John", "M001")
    member2 = Member("Jane", "M002")

    library.add_book(book1)
    library.add_book(book2)

    library.register_member(member1)
    library.register_member(member2)

    member1.borrow_book(book1)
    member2.borrow_book(book2)

    print(library)

if __name__ == '__main__':
    test_example()

```


- [Employee Management System](challenge_employeems.py)
    - Create a class structure for an employee management system. The system should manage employees, departments, and projects. Implement functionality to assign employees to departments and projects.
```py
class Employee:
    def __init__(self, name: str, employee_id: str) -> None:
        self.name = name
        self.employee_id = employee_id
        self.department = None
        self.projects = []

    def assign_department(self, department) -> None:
        # Implement the logic to assign an employee to a department

    def assign_project(self, project) -> None:
        # Implement the logic to assign an employee to a project

    def __str__(self) -> str:
        return f'Employee(name={self.name}, employee_id={self.employee_id})'

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee) -> None:
        # Implement the logic to add an employee to the department

    def __str__(self) -> str:
        return f'Department(name={self.name}, employees={len(self.employees)})'

class Project:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee) -> None:
        # Implement the logic to add an employee to the project

    def __str__(self) -> str:
        return f'Project(name={self.name}, employees={len(self.employees)})'

# Example Usage
def test_example() -> None:
    employee1 = Employee("Alice", "E001")
    employee2 = Employee("Bob", "E002")

    department = Department("Engineering")
    project = Project("Project X")

    department.add_employee(employee1)
    project.add_employee(employee1)

    department.add_employee(employee2)
    project.add_employee(employee2)

    print(department)
    print(project)
    print(employee1)
    print(employee2)

if __name__ == '__main__':
    test_example()

```


## Forward References in Class

- In Python, when you refer to a class that hasn't been fully defined yet or refer to the same class within a method, you use a string to specify the class name. This helps the interpreter understand the type without causing a NameError due to undefined references.
    - When you need to reference a class within its own definition (e.g., self-referential methods).
    - When you have a circular dependency between classes. Mutually dependent classes.
    - When referring to a class that is defined later in the code.
        - [Forward references](https://peps.python.org/pep-0484/).
        - [Stack:](https://stackoverflow.com/questions/55320236/does-python-evaluate-type-hinting-of-a-forward-reference)
- From Ptyhon 3.10 onwards, the `from __future__ import annotations` can be used to defer evaluations of type annotations, removing the need for string annotations.
```py
from __future__ import annotations

class Account:
    def __init__(self, customer, account_number):
        self.customer = customer
        self.account_number = account_number
        self.balance = 0.0

    def transfer(self, amount: float, target_account: Account) -> None:
        pass
```


## Decorators

### Introduction

- When need to extend or augment the functionality of a callable without modifying the callable itself we use decorators.
- This is a form of metaprogramming and is accomplished by wrapping one callable with another. Wrappers sit between callers and callables and perform operations before and or after calling the wrapped callable.
- Wrappers accept a callable object and retrun a callable matching the argument signature of the wrapped callable. The returned callable becomes the a replacement for the wrapped callable.
- Functions and methods are both callable objects.
- Shorthand syntax name: *Decorators*
- Used cases; Web Authentication.
\
&nbsp;
- In [decorator_intro.py](decorator_intro.py) *longhand syntax for wrapping a callable* demos how to manually wrap a function.
- `any_callable_function('a', 'b', 'c')` outputs the: `any_callable_function: with arguments: arg_a='a' arg_b='b' arg_c='c'`
\
&nbsp;
- Manual wrapping requires calling the `make_wrapper` function and passing the `any_callable_function` object.
- `wrapped_callable('a', 'b', 'c')` outputs the: `any_callable_function: with arguments: arg_a='A' arg_b='bbbbbbbbbb' arg_c='c'`
\
&nbsp;
- *wrapper with additional args* demos how the `make_wrapper_func_args` function accepts a callable to wrap and a keyword argument. The action argument is provided when the wrapper is created and accessible from the returned wrapper function. The `wrapped_callable` name will use *title* as the action.
- `wrapped_callable('a', 'b', 'c')` outputs the: `any_callable_func_args: with arguments: arg_a='A' arg_b='BBBBBBBBBB' arg_c='c'`
\
&nbsp;
- Wrappers with arguments are similar to [partial functions](https://docs.python.org/3/library/functools.html#functools.partial) where one or more arguments are pre-set. Which are useful for a wide range of use cases.


### Using the shorthand syntax: @decorator

- Decorators are a shorthand syntax for creating wrappers. Decorators are placed above a callable definition with a preceeding @ symbol. Following the @ symbol the decorator callable is called using the callable syntax (name).
- In [decorators.py](decorators.py) *using the shorthand syntax* demos how the decorator is called and returned instead of the original callable.
- `any_callable_function('a', 'b', 'c')` outputs the: `any_callable_function: with arguments: arg_a='A' arg_b='bbbbbbbbbb' arg_c='c'`
\
&nbsp;
- The decorator syntax consists of placing a name binding after an @ symbol. The example above doesn't directly call the decorator. Which is why the decorator is without parenthesis. Looks `@im_a_decorator` instead of `@im_a_decorator()`
- Simple decorator functions accept a function as an argument. More complex functions may have additional layers of wrapping. There are different reasons why additional wrapper layers might be added.

> [!NOTE]
> A general rule to determine if a decorator needs to be called is as follows: 
> Functions accepting a wrapped function directly do not need to be called. All others will need to be called according to their function signature with the arguments.

- Decorators require an additional function in order to allow arguments. The outermost function defines the required arguments and returns the next function. The remaining functions make the wrapper callable.
- `some_callable_function('a', 'b', 'c')` outputs the: `some_callable_function: with arguments: arg_a='X' arg_b='YYYYYYYYYY' arg_c='z'`
\
&nbsp;

- Decorators make it easier to effectively manage wrappers by defining them alongside the callable definition.
- The wrappers in the above examples match the argument signature of the wrapped callable. However, decorators are often applied to callables with unknown signatures.
- For this need to use packing/unpacking syntax to represent multiple positional and keyword arguments with individual arguments.

> [!TIP]
> The wrapper defines two arguments: `args` and `kwargs`. The single asterik in front of args instructs the interpreter to pack all positional arguments into args as a tuple.
> the double asterisk packs all keyword arguments into kwargs as a dictionary.

> [!NOTE]
> The names `args` and `kwargs` are common though, irrelevant to the packing/unpacking process.

- Creating generic decorators allows them to be reused across callables with different signatures.


### Chain of wrappers

- Decorators can be stacked to create a chain of wrappers. Decorators are evaluated by the inerpreter from bottom to top.
- In [decorators.py](decorators.py) *chain of wrappers* demonstrate how the decorator stacks works.
- In [decorators.py](decorators.py) *stacking is evaluted from bottom to top* demonstrate how the stacking is evaluted
- `print(b_callable('THIS IS THE WAY'))` outputs the: `This Is The Way lower string`
- `print(c_callable('THIS IS THE WAY'))` outputs the: `This Is The Way Lower String`


### Decorator interference

- Decorators can interfere with the metaprogramming of third-party libraries. Libraries such as flask rely on the names of callables. Wrapping a callable replaces the original callable with the wrapper including the name.
- In [decorators.py](decorators.py) *decorator interference*:
    - `print(something_sortb_slow.__name__)` outputs the: `something_sortb_slow`
    - `print(something_sorta_slow.__name__)` outputs the: `wrapper`
- In the second instance it displays the wrapper function name since the original function has been replaced by the wrapper function.
- This can cause errors in third-party libraries.
- `functools.wrap` in the Python's standard library can be used to rename the wrapper with the original name.
    - `print(something_sortc_slow.__name__)` outputs the: `something_sortc_slow`


## Challenge MessageClient

- Convert the MessageClient class into a context manager
- Following code must be run when entering the context.
```py
self.connection = socket.create_connection((self.host, self.port), timeout=5.0)
return self
```

- Following code muste be run when exiting the context.
```py
self.connection.close()
```

- Implement the redact decorator and apply it to the `send_message` method of the `MessageClient` class.
- Messages(type: bytes) starting with: 'TOP SECRET: ' must have all remaining characters replaced with an asterisk (*).
- Example:
```py
original = b'TOP SECRET: Aliens are invading!'
redacted = b'TOP SECRET: ********************'
```
- Messages that are not TOP SECRET must remain unchanged.
- Example
```py
original = b'Hey!'
redacted = b'Hey!'
```
- Messages must be redacted before being passed as an argument to the `send_message` method.
- Implement the `unredacted` method of the `MessageServer` class.
- Pass a lambda function to the `search` method and return all messages that are not redacted.

\
&nbsp;
\
&nbsp;


## Unittest

- Tests are created inside test cases. Test cases are created by subclassing the `unittest.TestCase` class. TestCase include methods for performing setup and teardown, making assertions, among others.
- The `unittest` module was based on a popular Java testing framework called jUnit. Unittest ignores many of Python's idioms in favor of mirroring junit, which followed Java's idioms. there are third-party Pythonic testing libraries such as [*Pytest*](https://docs.pytest.org/en/stable/).
- Pytest uses Python's assert keyword to make assertions rather than specific assertion methods. It also locates tests based on naming conventions which removes the need to subclass `unittest.TestCase`.


### Introduction

- The unittest module is Python's built-in testing [module](https://docs.python.org/3/library/unittest.html#module-unittest). Used to create and run unit and integration tests.
- All software contains developer made assumptions. Areas of code where assumptions are made:
    - Callable parameters and return types.
    - Object types.
    - Nullability
    - Idempotency.
    - Data structures.
- Erroneous assumptions can result in software defects of varying degrees of severity. Unittest enables developers to test the assumptions.
- It's designed around the notion of performing an action and making an assertion regarding the results.
- Actions are events which produce or change: objects and or external resources; resources including files, dbs etc, actions including operations, and callables.
- Actions are taken and assertions are made about the stats of the results. Assertions raise an exception when results don't match what's expected. Indicating that a codified assumption is no longer accurate.

| Action | Expected Result | Assertion |
| ----- | ----- | ----- |
| `int('10')` | 10 | `int('10')` equals 10 |
| `str(3.14)` | '3.14' | `str(3.14)` equals '3.14' |
| `int('no')` | ValueError | `int('no')` raises a ValueError |

- A basic unittest [example](./tests/test_assertion.py). # class TestExample
- Test cases represent concepts which can be tested as a single entity, sa objects, functions, and methods. Test methods can contain zero or more assertions. A test passes when all assertions inside the test method are successful.


### Test Runner

- The unittest module includes a mechanism for running tests called a test runner. The test runner is used to run or more tests test cases.
- In the example we called the tests from `unittest.main()` callable. By default it runs the tests from test casses defined in the current code file.
- The callable can be configured by providing keyword arguments to the callable, by specifying command line arguments, or both.


##### Using with CLI Flags

- Configurations can be specified as for the [guide](https://docs.python.org/3/library/unittest.html#command-line-options).
- `python3 test_assertion.py -v -f`


##### Using with Keyword Arguments

- Configurations can be specified as for the [guide](https://docs.python.org/3/library/unittest.html#unittest.main).
- `unittest.main(verbosity=2, failtest=True)`


#### Test Runner: CLI

- The test runner can be started by invoking the unittest module as a command line application. Including options to run one or more test modules, test cases, or test methods.
- `python3 -m tests.test_assertion.TestExample.test_is_number -v -f`
- `python3 -m tests.test_assertion -v -f`


#### Test Runner: Discovery

- The unittest module includes a [test-discovery](https://docs.python.org/3/library/unittest.html#test-discovery) mechanism based on file name patterns. Allowing multiple test caces inside a module to be run together.
- A real-world example of test [suite](https://github.com/python/cpython/blob/main/Lib/unittest/main.py).
- The location of `python3<ver>/unittest/test` is OS and install specific. `ls -lash /usr/local/lib/python3<ver>/unittest/test`
- `python3 -m unittest discover /usr/local/lib/python3<ver>/unittest/test "test*.py"` This command will search the dir for all files as specified.


### Test Cases

- The unittest module takes an obj-oriented approach to testing; introducing a base class used as a test building block called a test case.
- Test cases define a context for performing tests. Any concept which can be treated as a single unit can be a test case. Including: functions, class definitions, workflows, etc.
- Examples:
    ```py
    class TestSpecificFunction(unittest.TestCase):
        ''' Assumptions about a specific function are tested across one or more test methods. '''
    class TestSpecificClassDef(unittest.TestCase):
        ''' Assumptions about a specific class are tested across one or more test methods. '''
    class TestIndexWebPageLoad(unittest.TestCase):
        ''' Assumptions about a specific workflow are tested across one or more test methods. 
            Examples:
            - Does the index web page load?
            - Does the index web page return a successful status code?
            - ...
        '''
    ```

- A class becomes a test case by inheriting from [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase).
- Class definitions for test cases often include the name *Test* at the start or end of the class name.
- Examples:
    ```py
    class TestInt(unittest.TestCase): pass
    class IntTest(unittest.TestCase): pass
    class TestIndexWebPageLoad(unittest.TestCase): pass
    class SiteLoginProcessTest(unittest.TestCase): pass
    ```
- Tests are defined by creating methods with names starting with the word *test*. This naming convention is used by the test runner to identify tests. when the test runner encounters _test*_ methods it recognizes and runs them.


#### Test Cases: Assertions

- The unittest.TestCase base class defines methods for performing [*assertions*](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual). These methods are used to compare and inspect objects in different ways.
- Examples:
    - assertTrue
    - assertFlase
    - assertNone
    - assertEqual
- Tests use one or more of these assertion methods to test assumptions.
- [`test_assertion_methods.py`](./tests/test_assertion_methods.py)


#### Test Cases: Setup/Teardown

- Test cases may consist of many test methods. to reduce repeated code the TestCase base class includes setup and teardown methods. These methods are run before each test, allowing tests to use shared resources.
- This is commonly used to set up connections to external services such as databases.
- [`test_setup_teardown.py`](./tests/test_setup_teardown.py)


#### Test Cases: Skip Tests (Conditional Tests)

- Test methods can be conditionally skipped using decorator functions or TestCase methods. This is useful in scenarios where tests aren't required for a given OS, Python versions, etc.
- [`test_conditions.py`](./tests/test_conditions.py)


### Test Failures

- Incorrect assertions results in failinf test methods.
- Failed tests display the traceback in the console.
- [`test_failures.py`](./tests/test_failures.py)


## Mocking


### Introduction to Mock

- The unittest.mock module is Python's mocking and patching module.
- Used to replace objects with fake implementations during testing.
- Mock objects or mocks can replace objects with fake implementations and make asertions about how mock objects are used.
- Commonly used to replace objects and external resources such as files, dbs and web APIs.
- Replacing functionality with mock implementations allows code to be tested independently of it's dependencies.
- Key features of Mocks.
    - Mocks are callable.
        - Non-callable varients exists:
            - NonCallableMock
            - NonCallableMagicMock
    - Mocks create attributes and methods when first accessed.
    - Record all calls along with arguments.
    - Include assertion methods used to ensure calls are made as expected.
        - Failed assertions raise an AssertionError

```py
from unittest.mock import Mock

def greeter(name: str, display_callable: callable = print):
    '''
        Demo function to demo how to use a mock in place of another object.
    '''
    display_callable(f'Hello, {name}')

# This will display Hello, World in the console because the built-in print
# function is the default argument for the display_callable parameter.
greeter(name='Iroshan')

# Call again passing a mock as the display_callable.
display=Mock()

# This will not display in the console because the mock is called in
# place of the print function.
greeter(name='World', display_callable=display)

# Mocks include different assertion methods used to determine if the
# mock implementation is called as expected.

# Verify that the mock implementation of print is called with the expected
# argument value.
display.assert_called_with('Hello, World')

#################################
print('No assertion errors')
```

