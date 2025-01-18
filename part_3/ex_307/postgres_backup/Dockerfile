FROM postgres:latest

# Install curl for uploading to Google Cloud Storage
RUN apt-get update && apt-get install -y curl

# Copy the backup script to the container
COPY scripts/backup.sh /usr/src/app/backup.sh

# Make the backup script executable
RUN chmod +x /usr/src/app/backup.sh

# Set the entrypoint to the backup script
ENTRYPOINT ["/usr/src/app/backup.sh"]