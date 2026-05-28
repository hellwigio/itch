#!/bin/bash

for i in {1..10} 
do
	echo $(date +%T) $(ps -ef | wc -l)
	#sleep 5 
done

cat /proc/cpuinfo > cpuinfo

cat /etc/os-release | head -1 | awk -F"=" '{print $2}'

mkdir -p trash

touch trash/{50..100}.txt
