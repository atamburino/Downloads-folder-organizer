# Use an official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies file to the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . .

# Command to run the script
CMD ["python", "./fileFolderAutomator.py"]
