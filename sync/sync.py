"""
programa para sincronizar ficheiros e arquivos de uma pasta para outra periodicamente, mantendo ambas exatamente iguais

"""
import os
import shutil
import time
import hashlib
import argparse
from datetime import datetime

def log_action(message, log_file):
    """Logs actions to both console and a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    
    print(log_entry)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")

def get_file_hash(file_path):
    """Returns MD5 hash of a file to check for modifications."""
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
    except Exception as e:
        return None
    return hasher.hexdigest()

def sync_folders(source, replica, log_file):
    """Synchronizes the replica folder with the source folder."""
    if not os.path.exists(source):
        log_action(f"Source folder does not exist: {source}", log_file)
        return
    
    if not os.path.exists(replica):
        os.makedirs(replica)
        log_action(f"Created replica folder: {replica}", log_file)

    # Sync files & subdirectories from source → replica
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        replica_path = os.path.join(replica, item)

        if os.path.isdir(source_path):
            sync_folders(source_path, replica_path, log_file)
        else:
            # Copy if file does not exist or is modified
            if not os.path.exists(replica_path) or get_file_hash(source_path) != get_file_hash(replica_path):
                shutil.copy2(source_path, replica_path)
                log_action(f"Copied/Updated: {source_path} → {replica_path}", log_file)

    # Remove extra files & directories from replica
    for item in os.listdir(replica):
        replica_path = os.path.join(replica, item)
        source_path = os.path.join(source, item)

        if not os.path.exists(source_path):
            if os.path.isdir(replica_path):
                shutil.rmtree(replica_path)
                log_action(f"Removed directory: {replica_path}", log_file)
            else:
                os.remove(replica_path)
                log_action(f"Removed file: {replica_path}", log_file)

def main():
    parser = argparse.ArgumentParser(description="Folder Synchronization Script")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval (in seconds)")
    parser.add_argument("log_file", help="Path to the log file")

    args = parser.parse_args()

    log_action("Starting folder synchronization...", args.log_file)
    log_action(f"Source: {args.source}", args.log_file)
    log_action(f"Replica: {args.replica}", args.log_file)
    log_action(f"Sync Interval: {args.interval} seconds", args.log_file)

    while True:
        sync_folders(args.source, args.replica, args.log_file)
        log_action("Synchronization complete. Waiting for next cycle...\n\n", args.log_file)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()