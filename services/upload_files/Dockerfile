FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/upload_files/ ./services/upload_files/
COPY services/tools ./services/tools

CMD ["python", "-m", "services.upload_files.upload_main"]