#!/bin/bash

# Set the database name and the backup file name
DB_NAME="postgres"
BACKUP_FILE="database_backup.sql"
date=date=$(date '+%Y-%m-%d')

# Set the username and password for the database
DB_USERNAME="admin"
DB_PASSWORD="Nocnoc123456"

# Dump the database to a file
docker exec -i logapp_postgresql  /bin/bash -c "PGPASSWORD=$DB_PASSWORD  pg_dump --username $DB_USERNAME  $DB_NAME" > /var/DBbackup/$BACKUP_FILE-${date}


echo "Database has been done on ${date}" >> /var/DBbackup${date}.log

