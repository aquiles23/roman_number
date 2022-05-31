FROM python:3.10
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade -r /app/requirements.txt

COPY ./app/main.py /app/ 


