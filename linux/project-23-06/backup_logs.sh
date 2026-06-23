#!/bin/bash
#
LOG_DIR="/var/log/httpd"
BACKUP_DIR="/home/ec2-user/Backup_httpd"
MAX_BACKUP=3

DATE=$(date '+%Y%m%d-%T')
ARCHIVE="$BACKUP_DIR"/backup_httpd_logs-"$DATE".tar.gz

mkdir -p "$BACKUP_DIR"

tar -czf "$ARCHIVE" "$LOG_DIR"/*

systemctl stop httpd.service

rm -rf "$LOG_DIR"/*

systemctl start httpd.service

find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +"$MAX_BACKUP" -exec rm {} \;
