FROM python:3.6-alpine as it-api
RUN apk update && apk upgrade && apk add bash \
    busybox-extras \
    build-base

USER root
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "--config=gunicorn.py", "run:app"]
