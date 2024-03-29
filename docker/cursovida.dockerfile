FROM python:3.9.0-alpine
LABEL maintainer "value"
COPY . /var/www
WORKDIR /var/www
RUN apk update && apk add zlib-dev jpeg-dev gcc musl-dev python3-dev postgresql-dev 
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
EXPOSE  8000
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 cursoVida.wsgi
