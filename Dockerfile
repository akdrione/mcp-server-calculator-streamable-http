FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY calculator_streamable_http.py .

EXPOSE 8001

CMD ["python", "calculator_streamable_http.py"]
