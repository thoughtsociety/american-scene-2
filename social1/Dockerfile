FROM python:3.6.2

RUN mkdir -p /home/project/social1
WORKDIR /home/project/social1
COPY requirements.txt /home/project/social1
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . /home/project/social1

