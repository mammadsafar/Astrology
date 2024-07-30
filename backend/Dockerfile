FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install daphne
RUN pip install djoser
RUN pip install channels
RUN pip install django-ratelimit
RUN pip install kerykeion
RUN pip install pandas

COPY . /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
