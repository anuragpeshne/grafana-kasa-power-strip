FROM python:3-alpine

RUN apk update && \
      apk add --no-cache gcc \
      libffi-dev \
      openssl-dev \
      libxslt-dev \
      libxml2-dev \
      musl-dev \
      linux-headers \
      git

# Create work dir
RUN mkdir -p /opt/energy_monitor
WORKDIR /opt/energy_monitor

# setup pyHS100 - needed for polling the powerstrip
RUN git clone https://github.com/GadgetReactor/pyHS100.git && \
    cd pyHS100 && \
    pip install -r requirements.txt && \
    python setup.py install

COPY . .

# setup cron for logger
RUN mkdir -p /opt/energy_monitor/db
RUN touch /opt/energy_monitor/db/powerdb
COPY logger/logger_cron /etc/crontabs/root
CMD ["crond", "-f", "-d", "8"]

# setup data server
RUN pip install -r requirements.txt && \
    python server.py "/opt/energy_monitor/db/powerdb" &

EXPOSE 5000
