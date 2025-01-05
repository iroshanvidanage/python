# this example consist of three modules
# userman - a simulated user authentication system
# effects - applies image effects using the pillow library
# wsgi - a web application for uploading images and applying effects
# wsgi has been replaced by this file

# to start the web server
# flask --debug --app oop/wsgi.py run -h "0.0.0.0"

# sample creds un: admin, pd: magic

import os
from glob import glob
from pathlib import Path
from functools import wraps

# from flask import Flask, abort, flash, redirect, render_template, request, session, url_for
from markupsafe import escape
# from werkzeug.utils import secure_filename
# import the local supporting objects such as:
# blur, save, mode, fix_lab_path, and UserManagement
from .decorators_effects import *
from .decorators_userman import UserManagement
from . import *

# a fake user management service used to authenticate users.
user_management: UserManagement = UserManagement()
user_management.upsert_user('admin', 'magic')

session = []

# # app configuration
# app = Flask(__name__)
# # adjusts the lab URL path to work with the reverse proxy.
# app.after_request(fix_lab_path)

# # set the secret key to some random bytes, keep this secret
# app.secret_key = b'83jd9hakhfkeujdalefo'
# app.config['FILE_UPLOAD_FOLDER'] = Path(__file__).parent / 'static' / 'images'
# app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


def requires_login(func):
    ''' Decorator used to ensure users are logged in before accessing a route. '''
    '''
    Decorator requirements:

    1. Must work for multiple functions with varying argument signatures.
    2. The wrapper must maintain the name of the wrapped function.
    3. Wrapper logic:
        Call the wrapped function and return the results if the key 'username' exists in the global session object.

        Call the redirect function with the login url if the key 'username' does not exist in the global session object.
    4. Apply this decorator to the image function. Must be placed under the existing decorators.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # # answer
        # if 'username' not in session:
        #     return redirect(url_for('login'))
        if 'username' not in session:
            return login()
        return func(*args, **kwargs)
    return wrapper

# @app.route('/')
def index():
    # if 'username' in session:
    #     return redirect(url_for('image'))
    # return redirect(url_for('login'))

    if 'username' in session:
        return image()
    return login()


# @app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']

    #     if user_management.authenticate(username, password):
    #         session['username'] = username
    #         print(session)

    #         flash(f'Login successful!')
    #         return redirect(url_for('index'))
    #     else:
    #         flash(f'Login failed!')
    #         return render_template('login.html')
    # return render_template('login.html')


    username, password = map(input('Enter username and password seperated by a whitespace: '))

    if user_management.authenticate(username, password):
        session['username'] = username
        print(session)
        print(f'Login successful!')
        return index()
    else:
        print(f'Login failed!')
        return login()
    

# @app.route('/logout')
def logout():
    session.pop('username', None)
    # return redirect(url_for('index'))
    return index()


# @app.route('/image/', methods=['POST', 'GET'])
# @app.route('/image/<name>', methods=['GET'])
@requires_login
def image(name=None):
    # if request.method == 'POST':
    #     # Get all images
    #     if name is None:
    #         # Obtain a list of all images inside the FILE_UPLOAD_FOLDER
    #         images = [
    #             Path(_file).name for _file in
    #             glob(os.path.join(app.config['FILE_UPLOAD_FOLDER'], '*.png')) +
    #             glob(os.path.join(app.config['FILE_UPLOAD_FOLDER'], '*.jpg')) +
    #             glob(os.path.join(app.config['FILE_UPLOAD_FOLDER'], '*.jpeg'))
    #                   ]
    #         return render_template('images.html', images=images)
    #     # Get one image
    #     return render_template('image.html', image_name=name)
    
    # # Making it to this point implies a POST method
    # upload = request.files['image']
    # effect = request.form.get('effect', 'blur').lower()

    # if effect == 'blur':
    #     filtered_image = blur(upload, request.form.get('radius'))
    # elif effect == 'mode':
    #     filtered_image = mode(upload, request.form.get('size'))
    # else:
    #     # Escape to avoid injection issues should the logs be viewed in a browser
    #     app.logger.error(f'unexpected effect: {escape(effect)}')
    #     abort(500)

    # # Don't trust unsanitized user data
    # extension = secure_filename(upload.filename).rsplit('.', 1)[1]
    # # Requires write permissions to the FILE_UPLOAD_FOLDER
    # # save the file and return the generated name
    # name = save(filtered_image, extension, app.config['FILE_UPLOAD_FOLDER'])
    # # Redirect to the singular image page
    # return redirect(url_for('image', name=name, _method='GET'))
    print(f'Image page open successfully!')


# @app.errorhandler(404)
# def error_404(e):
#     return render_template('404.html'), 404


# @app.errorhandler(500)
# def error_500(e):
#     return render_template('500.html'), 500


# @app.errorhandler(InvalidImageError)
# def error_invalid_image(e):
#     return render_template('invalid-image.html'), 500



def test_example() -> None:
    return


if __name__ == '__main__':
    test_example()
