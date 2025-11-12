FROM python:3.8-slim

WORKDIR /app


COPY app/requirements.txt /app/
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    libffi-dev \
    zlib1g-dev \
    libjpeg-dev \
    netcat-traditional \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
COPY app /app
COPY .env /app/.env
EXPOSE 8020

COPY app/entrypoint.sh /entrypoint
RUN chmod +x /entrypoint
ENTRYPOINT ["/entrypoint"]
