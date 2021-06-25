#! /bin/bash

if [[ -z "${STRIP_IP}" ]]; then
  echo "\$STRIP_IP not set" > /dev/stderr
else
  power=$(/usr/local/bin/pyhs100 --strip --host $STRIP_IP emeter | tail -n 1)
  timestamp=$(date +%s)

  echo -e "$timestamp, $power"
fi
