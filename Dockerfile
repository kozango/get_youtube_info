# Dockerfile for keiei_youtube_info (経営中毒 YouTube コンシェルジュ)
FROM python:3.11-alpine

# Set workdir
WORKDIR /app

# Install build dependencies for pip packages
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Create output directory (if not exists)
RUN mkdir -p /app/output /app/output/transcripts

# Entrypoint for help
ENTRYPOINT ["python", "-m", "src.main"]
CMD ["--help"]
