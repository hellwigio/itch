#!/bin/bash
#
# В каталоге /opt/060326-ptm/name создаст 5 каталогов с именами Dir1 … Dir5 
# В каждый из созданных каталогов создаст 5 файлов с интервалом 5 секунд с именами File1.txt … File5.txt
# В каждый файл запишет текущие время в формате H-M-S
# По окончанию создания каждого каталога со списком файлов выводит на экран список файлов.

mkdir -p /opt/060326-ptm/name
cd /opt/060326-ptm/name

for i in {1..5}
do
    mkdir Dir$i
    for j in {1..5}
    do
        date +%T > File$i.txt
        sleep 5
    done
done

ls Dir*
