FROM python:3.10

WORKDIR /

RUN mkdir -p db/

RUN chmod -R 777 db/

COPY ./requirements.txt /anitrends/requirements.txt

RUN pip install -r /anitrends/requirements.txt
