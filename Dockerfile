# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY app /app

# ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8989", "application:app"]

FROM --platform=linux/amd64 python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    gfortran \
    libblas-dev \
    liblapack-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel

FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app/ .

EXPOSE 8989

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8989", "application:app"]

COPY app/ .

EXPOSE 8989

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8989", "application:app"]
