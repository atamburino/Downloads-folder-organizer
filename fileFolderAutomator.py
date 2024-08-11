import logging
import sqlite3

from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Source Folder = Folder to track
source_dir = "/Users/Windows-hater/Downloads"

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

class FileHandler(FileSystemEventHandler):
    def get_destination(self, ext):
        conn = sqlite3.connect('C:/Users/Windows-hater/OneDrive/Documents/Repos/Downloads-folder-organizer/FileMappings.db') # Connect to the database
        cursor = conn.cursor()
        cursor.execute("SELECT destination_folder FROM mappings WHERE file_extension = ?", (ext,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():  # Make sure it's a file
                    name = entry.name
                    _, ext = splitext(name)
                    ext = ext.lower()  # Handle extensions in a case-insensitive manner
                    destination = self.get_destination(ext)  # Use self to call the method
                    if destination:
                        move_file(destination, entry, name)
                        logging.info(f"Moved file '{name}' to '{destination}'")
                    else:
                        logging.info(f"No mapping found for extension '{ext}', file '{name}' skipped.")




# ! Watchdogs API Code (From Site)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()