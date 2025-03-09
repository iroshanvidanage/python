from unittest.mock import Mock

################### Requested Calls #########################

# Repeated calls can return different values by specifying a list as the side_effect arg.
# The return order matches the order of the objs in the list.
mock = Mock(side_effect=['a', 'b', 'c'])

# Each call returns the next object in the list.
assert mock() == 'a'
assert mock() == 'b'
assert mock() == 'c'
# Un-commenting this will give an error.
# print(mock())



################## Exceptions ################################

# Calls can raise exceptions by specifying as exception as the side_effect arg.
mock = Mock(side_effect=Exception('Exception raised by the side_effect'))

try:
    mock()
except Exception as e:
    print(e)


################## Exceptions in List ########################

# Exceptions in a listare raised when encountered.
mock = Mock(side_effect=['a', 'b', Exception('Exception in the list raised by the side_effect'), 'c'])

assert mock() == 'a'
assert mock() == 'b'
try:
    mock()
except Exception as e:
    print(e)
assert mock() == 'c'


##################### Functions ########################

def multiplier(a, b) -> float:
    ''' Multiply two numbers and return the result '''
    return a * b

# Side effects can be callables.
mock = Mock(side_effect=multiplier)

# Arguments passed to the mock are passed through to the callable
assert mock(10, 10) == 100

##############################
print('No assertion errors')