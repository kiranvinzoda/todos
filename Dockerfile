FROM python:3.10.4

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /app
COPY ./ /app/

CMD alembic upgrade head ; uvicorn main:app --host 0.0.0.0 --port 8000
