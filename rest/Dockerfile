FROM python:3.12-alpine
LABEL org.opencontainers.image.authors="lude4390@colorado.edu"

WORKDIR /srv

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN python -m pip install --no-cache-dir redis jsonpickle requests flask minio

COPY rest-server.py /srv/rest-server.py

EXPOSE 5000

CMD ["python3", "rest-server.py"]
