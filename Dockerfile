# # Use official Python base image
# FROM python:3.11-alpine

# # Set working directory inside container
# WORKDIR /app

# # Copy dependencies first
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the source code
# COPY . .

# # Set default command to run the CLI
# CMD ["python", "main.py"]




# v1.4 Multi stage build




# Stage 1: Build dependencies
FROM python:3.11-alpine as builder

# Set working directory inside container
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: Runtime image


FROM python:3.11-alpine

# Set working directory inside container
WORKDIR /app

COPY --from=builder /install /usr/local

# Copy the source code
COPY . .

# Set default command to run the CLI
CMD ["python", "main.py"]


