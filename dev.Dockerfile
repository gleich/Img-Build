# Base image with docker and python3.6 installed
FROM mattgleich/python-and-docker

# Image metadata
LABEL maintainer="matthewgleich@gmail.com"
LABEL description="Automatically build images anywhere that docker runs"

# Installing Git
RUN apt-get update
RUN apt-get -qq -y install git

# Installing requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 
COPY dev-requirements.txt dev-requirements.txt
RUN pip3 install -r dev-requirements.txt
RUN export GIT_PYTHON_REFRESH=quiet

# Copying over files
COPY /src /src
COPY /tests /tests
WORKDIR /tests

CMD [ "pytest", "--emoji" ]