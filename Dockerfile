FROM python:3.8-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r install.txt
CMD bash start