from unittest.mock import patch

def greeter(name: str) -> None:
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')


def main() -> None:
    # Patch can be used as a context manager.
    # The first argument is a target object to replace.
    # The target is a str representing the package.module.object
    with patch(f'builtins.print') as print_mock:
        # The builtin print callable will be replaced inside this code block.
        greeter('World')

        # Inspect the mock version of the print callable and determine if it 
        # was provided with the expected input.
        print_mock.assert_called_with('Hello, World')
        print_mock.assert_called_once()
    
    greeter('World')


if __name__ == '__main__':
    main()
