from prometheus_client import start_http_server, Counter
import logging
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configuration du logging
logging.basicConfig(filename='/var/log/app.log', level=logging.INFO)

# Compteur pour Prometheus
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        return get_secret_value_response['SecretString']
    except (NoCredentialsError, PartialCredentialsError):
        return None

def main():
    REQUEST_COUNT.inc()
    secret_message = get_secret('my_secret')
    if secret_message:
        message = f"Bienvenue chez Fintech Solutions! Secret: {secret_message}"
    else:
        message = "Bienvenue chez Fintech Solutions!"
    logging.info(message)
    print(message)
    return message


if __name__ == "__main__":
    start_http_server(8000)
    main()
