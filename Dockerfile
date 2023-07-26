FROM python:3.11-alpine



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY . .

RUN apk add poetry && poetry install --no-dev





CMD alembic upgrade head && \
    uvicorn server:app --host 0.0.0.0 --reload --proxy-headers && \
    gunicorn -k uvicorn.workers.UvicornWorker
