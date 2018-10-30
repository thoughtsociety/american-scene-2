FROM python:3.6.2

RUN mkdir -p /home/project/economy1
WORKDIR /home/project/economy1
COPY requirements.txt /home/project/economy1

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . /home/project/economy1

