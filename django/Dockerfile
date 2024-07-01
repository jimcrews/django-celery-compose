# pull official base image
FROM python:3.11-alpine as base

USER root
RUN apk add gcc python3-dev musl-dev libffi-dev curl

RUN mkdir /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN adduser -D weather-user
USER weather-user

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]