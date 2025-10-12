FROM python:3.10-slim

# Install semua dependency voice yang dibutuhkan Discord
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libffi-dev \
    libsodium-dev \
    opus-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
