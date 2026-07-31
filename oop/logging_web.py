import logging
import sys
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

#############################################################
# Configure the logger to use a more informative and structured format.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

handler.setFormatter(logging.Formatter('%(asctime)s\t%(levelname)s\t%(lineno)d\t%(funcName)s\t%(message)s'))
logger.addHandler(handler)

##############################################################

# request is a global used to store WSGI env vars which
# are accessible to route handlers.
request = {}

class Application:
    def __init__(self):
        self.path_handlers = {}

    def route(self, path):
        ''' A callable decorator used to register for the decorated callable.

            Args:
                path (str) | The path to register for the decorated callable.
        '''
        def wrap(handler, *args, **kwargs):
            ''' Args:
                handler (callable)  | The callable to call when a request matches the path
                                        provided to the route method.
                                        
                                    The handler function isn't passed to the route method directly.
                                    When the route method is used as a decorator the decorated callable is passed to this wrap function.
                
                args (tuple)        | Positional arguments to pass to the handler when called.
                kwargs (dict)       | Keyword arguments to pass to the handler when called.
            '''
            logging.info(f'Registering route for path: {path} with handler: {handler.__name__}')
            # Store a tuple containing the handler callable and any optional arguments.
            self.path_handlers[path] = (handler, args, kwargs)
        return wrap

    def __call__(self, environ, start_response):
        ''' The WSGI callable interface. This method is called by the WSGI server when a request is received.

            Args:
                environ (dict)      | The WSGI environment dictionary containing request information.
                start_response (callable) | A callable provided by the WSGI server to start the HTTP response.
        '''

        response_headers = [('Content-Type', 'text/plain')]
        request_url_path = environ.get('PATH_INFO', '')

        logging.info(f'Received request for path: {request_url_path}')

        # Attempt to locate the callable for the current path.
        # If missing this is a 404 -- file not found -- error.
        if request_url_path not in self.path_handlers:
            logging.info(f'(404) Path not found: {request_url_path}')
            start_response('404 Not Found', response_headers)
            return [f'{request_url_path} not found'.encode('utf-8')]

        try:
            # Unpack the handler callable and arguments
            handler, args, kwargs = self.path_handlers[request_url_path]

            # Set the global request binding to the environ
            global request
            request = environ

            # The route handler is now able to access the environment variables.
            response_body = handler(*args, **kwargs)

            # Call start_response only if the handler returned without error.
            start_response('200 OK', response_headers)

            # Log the successful handling of the request
            logging.info(f'(200) Successfully handled request for path: {request_url_path} with handler: {handler.__name__}')

            # Also log the response body as a debugging option.
            logging.debug(f'response_body; {response_body}')

            # WSGI requires the response body to be an iterable.
            return [response_body, b'\n']
        except Exception as e:
            logging.exception(f'(500) Failed running handler for path: {request_url_path} with error: {e}')
            start_response('500 Internal Server Error', response_headers)
            return [str(e).encode('utf-8')]

class QueryStringParser:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        query_string = environ['QUERY_STRING']

        logging.debug(f'Query string received: {query_string}')
        # Add the parsed query string to the environ dictionary for access by route handlers.
        # The Key QUERY_STRING_PARSED will be available to
        # applications called after this middleware.
        environ['QUERY_STRING_PARSED'] = query_string = parse_qs(query_string)

        logging.debug(f'Parsed query string: {query_string}')
        return self.wsgi_app(environ, start_response)


# Create a WSGI application instance
app = Application()

# Register the index function to the default path.
@app.route('/')
def index():
    return b'Hello, Welcome to the World!'

@app.route('/reverse-it')
def reverse_it():
    return request['QUERY_STRING_PARSED'].get('text', '')[::-1].encode('utf-8')
    # Correct answer
    # return request['QUERY_STRING_PARSED'].get('text', [])[0][::-1].encode('utf-8')

if __name__ == '__main__':
    server = make_server('', 5000, QueryStringParser(app))
    server.serve_forever()
