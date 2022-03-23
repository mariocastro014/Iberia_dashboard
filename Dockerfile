FROM python:3

ENV PORT 80
ENV HOST=0.0.0.0

EXPOSE 80

WORKDIR /app

ADD . /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app