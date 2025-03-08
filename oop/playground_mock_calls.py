from unittest.mock import Mock, call

############## Inspecting Calls ###############

fake_obj = Mock()

# Call with positional and keyword arguments.
fake_obj('Hi', 'There', who='World')

# Call without args.
fake_obj()

# The call_count reflects the number calls made to the mock.
print(fake_obj.call_count)
assert fake_obj.call_count == 2

# Inspecting calls more closely is done with the unittest.mock.call obj.
# call makes it easier to make assertions regarding how the mock was called.

# Comparisons can be made by providing the same arguments to call that were
# provided to the mock.

# The calls to obj produce the following list of calls.
expected_calls = [call('Hi', 'There', who='World'), call()]

# To ensure that cakks made to mock matches the expected.
print(fake_obj.assert_has_calls(expected_calls))

# By default the order of the calls must be matched.
fake_obj.assert_has_calls([call(), call('Hi', 'There', who='World')], any_order=True)

# This attribute stores the calls made to the mock in order.
print(fake_obj.call_args_list)

# Calliing the mock again.
fake_obj('a', 'z', lang='en', case='lower')

# This attribute stores the the arguments of the last call as a tuple.
print(fake_obj.call_args)

# The first element contains the positional args.
# The second element contains the keyword args.
assert fake_obj.call_args == (('a', 'z'), {'lang': 'en', 'case': 'lower'})

# Specific elements are accessible by name
assert fake_obj.call_args.args == ('a', 'z')
assert fake_obj.call_args.kwargs == {'lang': 'en', 'case': 'lower'}

# Mock records method calls separately.
fake_obj.fake_attr.fake_method('a')

# To display method calls
print(fake_obj.method_calls)

# To display all the calls.
print(fake_obj.mock_calls)

###############################################
print('No assertion errors')