# syntax=docker/dockerfile:1
FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "examples/main.py"]

