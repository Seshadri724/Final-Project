# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY src ./src
COPY api ./api
COPY models ./models

# Default model path can be overridden
ENV MODEL_PATH=models/model.joblib

EXPOSE 8000
CMD [ "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000" ]
