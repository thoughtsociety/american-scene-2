FROM python:3.6.2

RUN mkdir -p /home/project/economy
WORKDIR /home/project/economy
COPY requirements.txt /home/project/economy

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . /home/project/economy

