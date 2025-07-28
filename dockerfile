FROM python:3.12-slim

WORKDIR /app
COPY . /app

# Install system packages and awscli via pip
RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir awscli

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
