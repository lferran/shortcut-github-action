FROM python:3.8-slim-buster

WORKDIR /app

COPY src/main.py main.py

CMD ["python3", "/app/main.py"]