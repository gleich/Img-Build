# Base image
FROM python:3.6-stretch

# Image metadata
LABEL maintainer="matthewgleich@gmail.com"
LABEL description="Automatically build images anywhere that docker runs"

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Installing requirements
RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /src /src
WORKDIR /src
RUN rm -rf repos
RUN mkdir repos

CMD [ "python3", "main.py" ]
