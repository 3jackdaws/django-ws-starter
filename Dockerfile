FROM            python:3.6
MAINTAINER      Ian Murphy <ian.murphy@tektronix.com>
ENV             PYTHONUNBUFFERED TRUE

RUN             mkdir /app
WORKDIR         /app
ADD             . .

RUN             apt-get update && apt-get install -y inotify-tools
RUN             pip install -r requirements.txt

ENTRYPOINT      bash -c 'sh docker-entrypoint.sh'
