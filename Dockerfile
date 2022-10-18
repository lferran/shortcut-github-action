# Container image that runs your code
FROM python:3.8-slim-buster

COPY entrypoint.sh entrypoint.sh

COPY src/main.py main.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]