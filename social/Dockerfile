FROM python:3.6.2

RUN mkdir -p /home/project/social
WORKDIR /home/project/social
COPY requirements.txt /home/project/social
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . /home/project/social

