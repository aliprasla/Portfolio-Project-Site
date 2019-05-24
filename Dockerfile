FROM python:3.6.8-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/local/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .