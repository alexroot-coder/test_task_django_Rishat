FROM python:3.11-alpine

RUN mkdir app

WORKDIR app

ADD requirements.txt /app/

ENV HOME=/home

ENV APP_HOME=/home/app/

RUN mkdir $APP_HOME

RUN mkdir $APP_HOME/static

RUN pip install -r requirements.txt

ADD .. /app/

#ADD .env.docker  /app/.env

CMD gunicorn test_task.wsgi:application -b 0.0.0.0:8000