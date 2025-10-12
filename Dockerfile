FROM python:3.10

RUN apt-get update && apt-get install -y     ffmpeg     libffi-dev     libsodium-dev     libopus-dev     && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir discord.py PyNaCl ffmpeg-python

CMD ["python", "main.py"]
