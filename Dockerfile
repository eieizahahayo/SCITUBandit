FROM python:3
RUN mkdir /code
WORKDIR /code
CMD python3 manage.py runserver
