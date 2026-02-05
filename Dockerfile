FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY myproject /app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
