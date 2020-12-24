FROM python:3.6-stretch

# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# check our python environment
RUN python3 --version
RUN pip3 --version

# set the working directory for containers
WORKDIR  /usr/src/app/

# Installing python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 ./trainSave-jetson.py

# Copy all the files from the project’s root to the working directory
COPY . .

# Running Python Application
CMD ["python3", "./faceRecognize-jetson.py"]