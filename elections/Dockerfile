FROM python:3.6.2

RUN mkdir -p /home/project/elections
WORKDIR /home/project/elections
COPY requirements.txt /home/project/elections
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt


COPY . /home/project/elections

