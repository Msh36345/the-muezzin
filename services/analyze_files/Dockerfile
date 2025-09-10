FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/analyze_files/ ./services/analyze_files/
COPY services/tools ./services/tools

CMD ["python", "-m", "services.analyze_files.analyze_main"]