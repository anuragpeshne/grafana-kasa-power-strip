FROM python:3-slim

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y git bash cron rsyslog

# Create work dir
RUN mkdir -p /opt/energy_monitor
WORKDIR /opt/energy_monitor

COPY . .

# setup data server
RUN pip install -r requirements.txt
CMD ["python", "./server.py", "/data/powerdb"]
