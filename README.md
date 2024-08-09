# Downloads Folder Organizer

## Overview

The Downloads Folder Organizer is a Python script that automatically organizes files in your Downloads folder based on their file types. This script monitors your Downloads folder for new files and moves them to designated subfolders such as "Images" or "Documents" based on their file extensions.

## Features

- **Automatic File Organization**: Monitors the Downloads folder and automatically moves files to their respective directories.
- **Supported File Types**:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.tiff`, `.psd`, `.bmp`, `.heif`, `.ico`, `.avif`, and more.
  - **Documents**: `.doc`, `.docx`, `.odt`, `.pdf`, `.xls`, `.xlsx`, `.ppt`, `.pptx`.
- **File Name Uniqueness**: If a file with the same name already exists in the destination folder, the script appends a number to the filename to ensure it remains unique.
- **Cross-Platform**: The script can be adapted for both Windows and MacOS environments.

## Prerequisites

- Python 3.x
- The following Python packages:
  - `watchdog`
  - `shutil`
  - `os`

You can install the required packages using `pip`:
```bash
pip install watchdog
```

## Modify the Script:

Update the source_dir variable to the path of the folder you want to monitor (e.g., your Downloads folder).
Update the dest_dir_image and dest_dir_documents variables to the desired destination directories.

## Run the Script:

On Windows
```
python fileFolderAutomator.py
```

On MacOS/Linux:
```
python3 fileFolderAutomator.py
```

Stop the Script:

Press Ctrl+C in the terminal to stop the script when you're done.

## Potential Improvements
Add support for more file types (e.g., videos, audio, etc.).
Add error handling for file operations.
Create a GUI for easier configuration.

## Acknowledgements
This script uses the watchdog library for monitoring file system events.