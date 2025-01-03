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