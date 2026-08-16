FROM python:3.12-slim

WORKDIR /app

# TgCrypto needs a C compiler when no prebuilt wheel is available.
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
