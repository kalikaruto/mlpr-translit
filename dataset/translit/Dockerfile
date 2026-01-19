FROM python:3.10.13-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential curl git libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
    libffi-dev liblzma-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install pip version explicitly
RUN python -m pip install --no-cache-dir --upgrade pip==23.0.1

# Install dependencies only (cached layer)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /root/.cache /tmp/*

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

