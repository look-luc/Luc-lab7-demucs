FROM python:3.6-alpine
LABEL MAINTAINER="lude4390@colorado.edu"

WORKDIR /srv

RUN pip3 install redis jsonpickle requests flask minio

COPY rest-server.py /srv/rest-server.py

EXPOSE 5000

CMD ["python3", "rest-server.py"]
