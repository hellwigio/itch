#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <address>"
  exit 1
fi

address="$1"
failed_count=0

while true; do
  output="$(ping -c 1 -W 1 "$address" 2>&1)"
  status="$?"

  if [ "$status" -eq 0 ]; then
    failed_count=0
    ping_time="$(echo "$output" | awk "NR==2" | grep -o 'time=[0-9]*' | cut -d= -f2)"

    if [ $ping_time -lt 100 ]; then
      echo "Ping time is above 100 ms: $ping_time ms"
    fi
  else
    failed_count=$((failed_count + 1))

    if [ "$failed_count" -ge 3 ]; then
      echo "Ping failed for $failed_count consecutive packets"
    fi
  fi

  sleep 1
done
