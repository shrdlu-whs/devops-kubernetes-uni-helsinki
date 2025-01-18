#!/usr/bin/env bash
set -e

if [ $POSTGRES_USER ] && [ $POSTGRES_PASSWORD ] && [ $POSTGRES_HOST ] && [ $POSTGRES_BACKUP_BUCKET ] && [ $AUTH_TOKEN ]
then
  POSTGRESURL="postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:5432/postgres"
  echo "Dumping the database"
  datetoday=$(date -I)
  pg_dump -v $POSTGRESURL > /dump/backup.sql
   curl -X POST --data-binary @/dump/backup.sql \
     -H "Authorization: Bearer $AUTH_TOKEN" \
     -H "Content-Type: application/sql" \
     "https://storage.googleapis.com/upload/storage/v1/b/$POSTGRES_BACKUP_BUCKET/o?uploadType=media&name=backup-$datetoday.sql"
fi