FROM python:3.8-slim-buster

WORKDIR /action

COPY entrypoint.sh entrypoint.sh

COPY src/main.py main.py

ENTRYPOINT ["/action/entrypoint.sh"]