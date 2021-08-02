FROM python:3-slim

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y git bash cron rsyslog

# Create work dir
RUN mkdir -p /opt/energy_monitor/logger
WORKDIR /opt/energy_monitor/logger

# setup pyHS100 - needed for polling the powerstrip
RUN git clone https://github.com/GadgetReactor/pyHS100.git && \
    cd pyHS100 && \
    pip install -r requirements.txt && \
    python setup.py install

COPY . .

# setup cron for logger
RUN mkdir -p /data
RUN touch /data/powerdb
COPY ./logger_cron /etc/crontabs/root
RUN ["service", "cron", "start"]
