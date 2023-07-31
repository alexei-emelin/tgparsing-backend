#!bin/sh
alembic upgrade head && \
uvicorn server:app --host 0.0.0.0 --reload --proxy-headers && \
gunicorn -k uvicorn.workers.UvicornWorker