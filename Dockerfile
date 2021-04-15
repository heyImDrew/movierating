FROM python:3.8.5
ENV PYTHONUNBUFFERED=1
WORKDIR /movierating
COPY requirements.txt /movierating/
RUN pip install -r requirements.txt
COPY . /movierating/