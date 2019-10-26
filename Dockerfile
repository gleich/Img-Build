# Base image with docker and python3.6 installed
FROM mattgleich/python-and-docker

# Image metadata
LABEL maintainer="matthewgleich@gmail.com"
LABEL description="Automatically build images anywhere that docker runs"

# Installing requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

CMD [ "python3", "main.py" ]
