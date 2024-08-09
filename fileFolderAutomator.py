import os
import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "/Users/Windows-hater/Downloads"

#Testing loopign through files
with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)

class FileHandler(FileSystemEventHandler):
    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_image_files(entry, name) #Image files
                self.check_document_files(entry, name) #Dc files

# Watchdogs Example API Usage Code
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    logging.info(f'start watching directory {path!r}')
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()