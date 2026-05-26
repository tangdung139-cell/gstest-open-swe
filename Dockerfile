# Use the official Python 3.11 slim image as base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the application's port
EXPOSE 8000

# Specify the command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]