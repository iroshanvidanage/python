# author    https://github.com/iroshanvidanage
# date      08/18/2024

FROM python:3.8.0-slim

WORKDIR /app

ADD . /app

RUN pip3 install --upgrade pip3 && pip install -r requirements.txt

# gunicorn is used to run the flask application
# port is defaulted to 8000
# reload will restart the workers
# the application is being deployed to heroku
CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload