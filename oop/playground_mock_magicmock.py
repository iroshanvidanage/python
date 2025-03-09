from unittest.mock import call, Mock, MagicMock

mock = Mock()

# Invoke a magic method by passing the mock obj to he int callable.
# int will check the provided obj for a method named __int__
try:
    # Because mock doesn't implement magic methods this call with fail.
    # The following call produces:
    # TypeError: int() argument must be a string, a bytes-like obj or a number, not 'Mock'
    int(mock)
except TypeError:
    print('Mock objs do not implement magic methods by default')


# MagicMock is Mock with the addition of some default value for many magic methods.
mock = MagicMock()

# MagicMock returns a default int of 1
assert int(mock) == 1

# Assertions can be made against magic methods.
mock.__int__.assert_called_once()

# Values can be changed by setting the return_value of a specific magic method.
mock.__int__.return_value = 5_000
assert int(mock) == 5_000

# MagicMock returns a default len of 0
assert len(mock) == 0
mock.__len__.return_value = 10
assert len(mock) == 10

# MagicMock returns a default float of 1.0
assert float(mock) == 1.0
mock.__float__.return_value = 3.14
assert float(mock) == 3.14

# MagicMock returns a default bool of True
assert bool(mock) == True
mock.__bool__.return_value = False
assert bool(mock) == False

# MagicMock returns a default value of False when searching a sequence
assert ';)' not in mock
mock.__contains__.return_value = True
assert ';)' in mock

# MagicMock returns an empty list by default.
assert list(mock) == []
mock.__iter__.return_value = ['a', 'b', 'c']
assert list(mock) == ['a', 'b', 'c']

# Calling MagicMock obj is mostly the same as Mock.
# With an exception for calls made to magic methods.
# MagickMock tracks calls made to magic methods independently.
# Reset the mock to start with zero calls.
print(mock.mock_calls)

mock.reset_mock()

# Call the int method.
# Call 1
int(mock)

# The method_calls property stores calls to methods and attributes, and their methods and attributes.
# Calls to magic methods don't appear in the method_calls attribute.
assert mock.method_calls == []

# The mock_calls attribute tracks calls to:
# - A mock object
# - A mock object's method
# - A mock object's magic methods
assert mock.mock_calls == [call.__int__()]

# Call 2
mock.fake_method('a')

# Call 3
mock('b')

# method_calls contains only the method call from: Call 2.
assert mock.method_calls == [call.fake_method('a')]

# mock_calls contains all three calls.
print(mock.mock_calls)
#########################################
print('No assertion errors')
