# Use official Python base image
FROM python:3.11-alpine

# Set working directory inside container
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Set default command to run the CLI
CMD ["python", "main.py"]
