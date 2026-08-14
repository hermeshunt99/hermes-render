FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git curl wget sqlite3 build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs

RUN pip install --no-cache-dir hermes-agent

COPY server.py .

EXPOSE 7860

CMD ["python3", "server.py"]
