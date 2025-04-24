FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.__main__:app", "--host", "0.0.0.0", "--port", "8000"]