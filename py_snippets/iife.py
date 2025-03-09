# Immediately Invoked Function Expression
# IIFE

# Creates a decorator which takes a function and calls it immediately.
# This decorator is a lambda decorator.
@lambda _: _()
def function() -> str:
    print('The function was called')
    return 'function value'

# This snippet will call the function without explicitly calling the function.

# And it will return the value which will be assigned to the function name.
print(function)