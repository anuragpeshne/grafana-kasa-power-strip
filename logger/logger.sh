#! /bin/bash

if [ -z $STRIP_IP ];
then 
  power=$(/usr/local/bin/pyhs100 --strip --host $STRIP_IP emeter | tail -n 1)
  timestamp=$(date +%s)

  echo -e "$timestamp, $power"
else
  echo "\$STRIP_IP not set" > /dev/stderr
fi
