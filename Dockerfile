FROM python:3.10-alpine as it-api
RUN apk update && apk upgrade && apk add bash \
    busybox-extras
USER root
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENTRYPOINT ["python", "run.py"]
