import random
from unittest.mock import Mock

fake_obj = Mock()


# To ensure the mock was not called.
# fake_obj()
fake_obj.assert_not_called()

# Call the mock obj to record the call.
fake_obj('Hi', 'There')
# fake_obj()

# To ensure the mock was called at least once.
fake_obj.assert_called()

# To ensure the mock was called only once.
fake_obj.assert_called_once()

# ensure the mock was called at least once with the arguments passed.
fake_obj.assert_called_with('Hi', 'There')

# ensure the mock was called only once with the arguments passed.
fake_obj.assert_called_once_with('Hi', 'There')

# To reset the previous calls.
fake_obj.reset_mock()

fake_obj.assert_not_called()

print('No assertion errors')


# Try this by commenting/uncommenting the assertions and different objs.