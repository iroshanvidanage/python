# author    https://github.com/iroshanvidanage
# date      08/17/2024


from models import models
from flask import Flask, request, render_template, redirect

DATABASE = 'employee_db.db'
app = Flask(__name__)





if __name__ == '__main__':
    app.run(host='0.0.0.0')
