FROM python:3.8.5
WORKDIR /code
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./ .
RUN echo yes | python manage.py collectstatic
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000