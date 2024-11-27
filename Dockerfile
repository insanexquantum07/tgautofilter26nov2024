FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /tgautofilter26nov2024
WORKDIR /tgautofilter26nov2024
COPY . /tgautofilter26nov2024
CMD ["python", "bot.py"]