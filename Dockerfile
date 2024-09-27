FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer l'agent CloudWatch
RUN apt-get update && \
    apt-get install -y awslogs && \
    rm -rf /var/lib/apt/lists/*

# Configurer l'agent CloudWatch
COPY awslogs.conf /etc/awslogs/awslogs.conf

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
