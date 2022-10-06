# For a lightweight Linux system with Python already installed
FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

# Create a folder called /app in our virtual OS
WORKDIR /app

COPY requirements.txt require.txt

RUN pip3 install -r require.txt

COPY . .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]