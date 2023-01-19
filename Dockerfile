FROM debian:11.6-slim

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN set -eux; \
    apt-get update; \
    apt-get -y dist-upgrade; \
    apt-get install -y --no-install-recommends python-is-python3 python3-pip python3-psycopg2; \
    apt-get clean all; \
    rm -r /var/lib/apt/lists /var/cache/apt/archives

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "app:app", "--access-logfile", "-"]
