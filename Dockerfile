FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY config/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port the server runs on
EXPOSE 8080

# Command to run the server
CMD ["python", "core/run_server.py"]
