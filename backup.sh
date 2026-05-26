#!/bin/bash

# Define the source directory and the backup directory
SOURCE_DIR="data"
BACKUP_DIR="backups"

# Create the backups directory if it does not exist
if [ ! -d "$BACKUP_DIR" ]; then
  mkdir -p "$BACKUP_DIR"
fi

# Create a timestamped backup file
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
backup_file="$BACKUP_DIR/backup_$timestamp.tar.gz"

# Compress the data directory into the backup file
tar -czf "$backup_file" "$SOURCE_DIR"

echo "Backup completed: $backup_file"