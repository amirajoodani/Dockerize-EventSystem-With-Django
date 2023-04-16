#!/bin/bash

BACKUP_FILE="database_backup.sql"
date=date=$(date '+%Y-%m-%d')

docker cp /var/DBbackup/$BACKUP_FILE-${date}   pgadmin4:/var/lib/pgadmin/storage/noc_sadadpsp.ir
echo "Database backup copy to container${date}" >> /var/DBbackup${date}.log
