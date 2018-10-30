FROM python:3.6.2

RUN mkdir -p /home/project/elections1
WORKDIR /home/project/elections1
COPY requirements.txt /home/project/elections1
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt


COPY . /home/project/elections1

