FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

# ✅ Correct installation of awscli with apt-get
RUN apt-get update && \
    apt-get install -y awscli && \
    rm -rf /var/lib/apt/lists/*

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Run your app
CMD ["python3", "app.py"]
