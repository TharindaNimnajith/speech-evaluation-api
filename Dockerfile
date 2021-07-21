FROM python:3.8-slim-buster

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install gunicorn

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc libsndfile1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
