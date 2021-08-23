# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

EXPOSE 8000


# Copy the current directory contents into the container at /app
COPY . /app/

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD sh ./entrypoint.sh

# terminal
#create image - # docker build . -t sample-api:1.0
#
# docker image tag sample-api:1.0 <ecr>/sample-api:1.0
# docker image push <ecr>/sample-api:1.0
# create lambda - container image
# add trigger to lambda - api gateway