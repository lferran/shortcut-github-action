FROM python:3.8-slim-buster

COPY entrypoint.sh entrypoint.sh

COPY src/main.py main.py

ENTRYPOINT ["/entrypoint.sh"]