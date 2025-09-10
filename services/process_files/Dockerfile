FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/process_files/ ./services/process_files/
COPY services/tools ./services/tools
COPY podcasts/ ./podcasts

CMD ["python", "-m", "services.process_files.process_main"]