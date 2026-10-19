FROM xserrat/facebook-demucs:latest

LABEL MAINTAINER="your-email@colorado.edu"

RUN pip3 install --no-cache-dir --upgrade minio redis requests

WORKDIR /srv

COPY worker-server.py /srv/worker-server.py

CMD ["python3", "worker-server.py"]
