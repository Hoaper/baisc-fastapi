FROM python:3.9

WORKDIR /python-app

COPY requirements.txt /python-app/

COPY . .


RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]
