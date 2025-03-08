import random
from unittest.mock import Mock

######################## Callables ###########################
fake_obj = Mock()

# Mocks can be called with any arguments.
fake_obj('a', 'b', z=True)
fake_obj(1, 2)
fake_obj()

# Mocks dynamically create attributes and methods when accessed.
fake_obj.fake_method()
fake_obj.fake_method(1, 2, 3, 4)
fake_obj.fake_method(z=True, x=False)

fake_obj.fake_attribute.fake_method()

######################## Return Values ######################

# Mock objs can return predefined values.

## Keyword args

# The return_value arg specifies the value to return when the mock is called.
calc_pi = Mock(return_value=3.14159)

## Attribute

# The return_value attribute can be set after the mock is created.
calc_pi2 = Mock()

calc_pi2.return_value=3.14159

## Method Return Values

mock_value = Mock()

# The return value attribute can be set on the mock method.
mock_value.fake_attribute.fake_method.return_value = 'Method to Madness'

def main():
    # Calls will will now return the specified value.
    assert calc_pi() == 3.14159

    # Calls will will now return the specified value.
    assert calc_pi2() == 3.14159

    # Calls will will now return the specified value.
    assert mock_value.fake_attribute.fake_method() == 'Method to Madness'



if __name__ == '__main__':
    main()
    print('No assertion errors')