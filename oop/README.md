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

> [!ERROR]
> `TypeError: Can't instantiate abstract class Text with abstract method render`

- The derived class must implement the interface in the abstract base class.
- The standard library includes a module named abc used for creating abstract base classes.
- The `Renderable` class derives from the ABC (Abstract BaseClass) type and uses the abstract method decorator to mark the render method as abstract.
- The `Renderable` class cannot be directly instantiated. It must be derived and its abstract methods must be implemented.
- It ensures that classes with `Renderable` in the base class hierarchy msut be implement the render method.

