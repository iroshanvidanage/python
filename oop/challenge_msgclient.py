## Challenge MessageClient
'''
- Convert the MessageClient class into a context manager
- Following code must be run when entering the context.
```py
self.connection = socket.create_connection((self.host, self.port), timeout=5.0)
return self
```

- Following code muste be run when exiting the context.
```py
self.connection.close()
```

- Implement the redact decorator and apply it to the `send_message` method of the `MessageClient` class.
- Messages(type: bytes) starting with: 'TOP SECRET: ' must have all remaining characters replaced with an asterisk (*).
- Example:
```py
original = b'TOP SECRET: Aliens are invading!'
redacted = b'TOP SECRET: ********************'
```
- Messages that are not TOP SECRET must remain unchanged.
- Example
```py
original = b'Hey!'
redacted = b'Hey!'
```
- Messages must be redacted before being passed as an argument to the `send_message` method.
- Implement the `unredacted` method of the `MessageServer` class.
- Pass a lambda function to the `search` method and return all messages that are not redacted.
'''


#########################################################################################
## script starts here
#########################################################################################

import socket, threading, time
from functools import wraps

class MessageServer:

    def __init__(self, host: str='127.0.0.1', port: int=5000) -> None:
        self.host = host
        self.port = port
        self.msgs = []
    
    def serve(self) -> None:
        ''' A basic TCP/IP listener
            Listens on the supplied host/port for binary data.
        '''

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen(1)
            while True:
                conn, adr = sock.accept()
                with conn:
                    while (mess := conn.recv(1024)):
                        # Stroe all the messages.
                        self.msgs.append(mess)
                        # Echo the message back to the client
                        conn.sendall(mess)
    
    def serve_forever(self, **kwargs) -> None:
        ''' Runs the message_server function in a background thread.
            Must be running before the client can be used.
        '''
        server = threading.Thread(target=self.serve, kwargs=kwargs, name='nerwork_server', daemon=True)
        server.start()
    
    def search(self, fn: callable) -> list:
        '''
            Args:
                fn  | A callable that accepts a byte objects and returns a boolean.
            
            Returns:
                A list of messages that return True when passed to the callable.
        '''
        return [msg for msg in self.msgs if fn(msg)]
    
    def unredacted(self):
        '''
            Returns:
                A list of messages that are not redacted in the order they were received.
            
            >>> server = MessageServer()
            >>> server.msgs = [b'TOP SECRET: *', b'HEY!', b'Sup.', b'TOP SECRET: **']
            >>> server.unredacted()
            [b'HEY!', b'Sup.']
        '''


def redact(function):
    ''' A decorator used to redact messages sent via the send_message method of the MessageClient.
        Messages are expected to be bytes objects. NOT str objects.
    '''
    @wraps(function)
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return function(*args, **kwargs)

        string_data = args[0].decode('utf-8')

        if 'TOP SECRET: ' not in string_data:
            return function(*args, **kwargs)
        
        string_data = string_data.split('TOP SECRET: ')
        string_data[1] = '*' * len(string_data[1])
        args[0] = 'TOP SECRET: '.join(string_data).encode('utf-8')

        return function(*args, **kwargs)
    return wrapper


class MessageClient:
    '''
        >>> port = 1337
        >>> server = MessageServer(port=port)
        >>> server.serve_forever()

        wait a second for the thread to get the server running.
        >>> import time; time.sleep(1.0)

        >>> with MessageClient(port=port) as client:
        ...     messages = [
        ...         b'TOP SECRET: Aliens are invading!.',
        ...         b'Hey!',
        ...         b'Sup.',
        ...         b'TOP SECRET: The universe is going to collapse.'
        ...     ]
        ...     for message in messages:
        ...         print(client.send_message(message))
        b'TOP SECRET: *********************'
        b'Hey!'
        b'Sup.'
        b'TOP SECRET: **********************************
    '''
    def __init__(self, host: str='127.0.0.1', port: int=5000) -> None:
        self.connection = None
        self.host = host
        self.port = port

    def __enter__(self) -> 'MessageClient':
        self.connection = socket.create_connection((self.host, self.port), timeout=5.0)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.close()
    
    @redact
    def send_message(self, message: bytes) -> bytes:
        self.connection.sendall(message)
        return self.connection.recv(1024)


def test_example() -> None:
    port = 5000
    server = MessageServer(port=port)
    server.serve_forever()
    time.sleep(1.0)

    with MessageClient(port=port) as client:
        messages = [
            b'TOP SECRET: Aliens are invading!.',
            b'Hey!',
            b'Sup.',
            b'TOP SECRET: The universe is going to collapse.'
        ]
        for message in messages:
            print(client.send_message(message))



if __name__ == '__main__':
    test_example()