FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install google-cloud-firestore
RUN pip install firebase-admin

COPY ./app /app
