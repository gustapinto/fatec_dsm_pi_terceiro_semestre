FROM python:3.10

WORKDIR /consumidor

RUN mkdir -p db/

RUN chmod -R 777 db/

COPY ./requirements.txt /consumidor/requirements.txt

RUN pip install -r requirements.txt
