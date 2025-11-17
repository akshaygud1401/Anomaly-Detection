FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app /app

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8989", "application:app"]