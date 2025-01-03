# decorators

from rich import print

# longhand syntax for wrapping a callable

def any_callable_function(arg_a, arg_b, arg_c=':)'):
    print(f'[blue]any_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')

def make_wrapper(function):
    def wrapper(arg_a, arg_b, arg_c=None):
        print(f'[blue]any_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')
        print()
        return function(arg_a.upper(), arg_b * 10, arg_c)
    return wrapper


print(f'Without the decorator:')
any_callable_function('a', 'b', 'c')
print()
print(f'With the decorator:')
wrapped_callable: make_wrapper = make_wrapper(any_callable_function)
wrapped_callable('a', 'b', 'c')
print()


# wrapper with additional args

def any_callable_func_args(arg_a, arg_b, arg_c=':)'):
    print(f'[blue]any_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')

def make_wrapper_func_args(function, action=None):
    def wrapper(arg_a, arg_b, arg_c=None):
        print(f'[blue]any_callable_function[/blue]: with arguments: {arg_a=} {arg_b=} {arg_c=}')
        print()
        if action in 'upper lower title'.split():
            arg_a = getattr(arg_a, action)()
            arg_b = getattr(arg_b, action)()
        return function(arg_a, arg_b * 10, arg_c)
    return wrapper


print(f'Without the decorator:')
any_callable_func_args('a', 'b', 'c')
print()
print(f'With the decorator:')
wrapped_callable: make_wrapper_func_args = make_wrapper_func_args(any_callable_func_args, 'title')
wrapped_callable('a', 'b', 'c')
print()