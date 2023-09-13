# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY test.py stegano.py ./
COPY templates/ ./templates
COPY static/ ./static

EXPOSE 80

ENTRYPOINT ["python", "test.py"]