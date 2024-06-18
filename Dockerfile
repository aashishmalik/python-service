# Use official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app.py .

EXPOSE 9090
# Command to run the application
CMD ["python", "app.py"]
