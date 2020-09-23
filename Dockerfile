FROM python:alpine 
MAINTAINER Trytechlabs

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add gcc musl-dev postgresql-dev python3-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user
