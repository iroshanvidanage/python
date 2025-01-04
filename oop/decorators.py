# decorators

from rich import print

# using the shorthand syntax

def im_a_decorator(function):
    def wrapper(arg_a, arg_b, arg_c=None):
        print(f'[blue]any_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')
        print()
        return function(arg_a.upper(), arg_b * 10, arg_c)
    return wrapper


@im_a_decorator
def any_callable_function(arg_a, arg_b, arg_c=':)'):
    print(f'[blue]any_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')


any_callable_function('a', 'b', 'c')


# directly called decorators

def decorator_with_args(action=None):
    def make_wrapper(function):
        def wrapper(arg_a, arg_b, arg_c=None):
            print(f'[blue]any_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')
            print()
            if action in 'upper lower title'.split():
                arg_a = getattr(arg_a, action)()
                arg_b = getattr(arg_b, action)()
        
            return function(arg_a, arg_b * 10, arg_c)
        return wrapper
    return make_wrapper


@decorator_with_args('upper')
def some_callable_function(arg_a, arg_b, arg_c=':)'):
    print(f'[blue]some_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')


some_callable_function('x', 'y', 'z')


# generic decorator


def generic_decorator(action=None):
    def make_wrapper(function):
        def wrapper(*args, **kwargs):
            print(f'[blue]wrapper[/blue] with arguments: {args=} {kwargs=}')
            if len(args) >= 2:
                args = list(args)
                args[0] = getattr(args[0], action)()
                args[1] = getattr(args[1], action)()

            return function(*args, **kwargs)
        return wrapper
    return make_wrapper


@generic_decorator('upper')
def a_callable(arg_a, arg_b, arg_c=':)', arg_d=':D'):
    print(f'[blue]a_callable[/blue]: {arg_a=} {arg_b=} {arg_c=} {arg_d=}',  end='\n\n')

@generic_decorator('title')
def b_callable(arg_a, arg_b, arg_c, arg_d=':D', arg_e=True):
    print(f'[red]b_callable[/red]: {arg_a=} {arg_b=} {arg_c=} {arg_d=} {arg_e=}',  end='\n\n')

@generic_decorator('upper')
def c_callable(arg_a, arg_b, arg_c=':)', arg_d=':D'):
    print(f'[green]c_callable[/green]: {arg_a=} {arg_b=} {arg_c=} {arg_d=}',  end='\n\n')

a_callable('this is the way', 'Hello')
b_callable('This developer', 'gets home late', 'what to do')
c_callable('Happy coding', 'my friend', arg_d='hungry for code')


# chain of wrappers


def title_case(function):
    def wrapper(text: str):
        return function(text).title()
    return wrapper

def exclaim_it(function):
    def wrapper(text: str):
        return f'{function(text)}!'
    return wrapper

def add_string(arg_text: str):
    def make_wrapper(function):
        def wrapper(text: str):
            return f'{function(text)} {arg_text}'
        return wrapper
    return make_wrapper


@exclaim_it
@title_case
def a_callable(text: str):
    return text.lower()

print(f'\nDecorator stacking:\n')
print(a_callable('THIS IS THE WAY'))

## stacking is evaluted from bottom to top

@add_string('lower string')
@title_case
def b_callable(text: str):
    return text

@title_case
@add_string('lower string')
def c_callable(text: str):
    return text

print(f'\nDecorator stacking example 2:\n')
print(b_callable('THIS IS THE WAY'))

print(f'\nDecorator stacking example 3:\n')
print(c_callable('THIS IS THE WAY'))


# timing the decorated callable

import time

def timer(function):
    def wrapper():
        start = time.perf_counter()
        fnout = function()
        close = time.perf_counter()
        print(f'{function.__name__} completed in {close - start:0.5f} seconds.')
        return fnout
    return wrapper

@timer
def something_sorta_slow():
    return ''.join([
        str(n) for n in range(1_000_000) if n % 10_000 == 0.0
    ])


print(f'\n[green]something_sorta_slow[/green]')
something_sorta_slow()


# decorator interference


def something_sortb_slow():
    return ''.join([
        str(n) for n in range(1_000_000) if n % 10_000 == 0.0
    ])

print(f'\n[green]Without decorator[/green]')
print(something_sortb_slow.__name__)

print(f'\n[green]With decorator[/green]')
print(something_sorta_slow.__name__)

# rename the wrapper

from functools import wraps

def timerb(function):

    @wraps(function)
    def wrapper():
        start = time.perf_counter()
        fnout = function()
        close = time.perf_counter()
        print(f'{function.__name__} completed in {close - start:0.5f} seconds.')
        return fnout
    return wrapper

@timerb
def something_sortc_slow():
    return ''.join([
        str(n) for n in range(1_000_000) if n % 10_000 == 0.0
    ])

print(f'\n[green]With wrapper renamed[/green]')
print(something_sortc_slow.__name__)