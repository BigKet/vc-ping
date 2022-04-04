FROM python:3.10.1

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
CMD ["python3","main.py"]