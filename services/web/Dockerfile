# pull base image
FROM python:3.10.7-slim-buster

# set work directory
WORKDIR /usr/src/app

# set env variables
# prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevent python from buffering to stdout and stderr
ENV PYTHONUNBUFFERED 1

# isntall system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
Run pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# run entryoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
