# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
COPY .env /app/
RUN pip install -r requirements.txt
COPY ./app/ /app/