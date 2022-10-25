FROM python:3.8-alpine

LABEL name="getnet-py"
LABEL version="1.0.4"
LABEL description="A Getnet Santander SDK"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apk add --update --no-cache \
    build-base \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    zlib-dev \
    openssl-dev \
    && rm -rf /var/cache/apk/*

RUN pip install --upgrade --no-cache-dir pip pipenv setuptools wheel twine

ADD Pipfile Pipfile.lock /getnet-py/
WORKDIR /getnet-py/
RUN pipenv lock --dev -r > requirements.txt && pip install --no-cache-dir -r requirements.txt

ADD . /getnet-py/
RUN pip install --no-cache-dir /getnet-py