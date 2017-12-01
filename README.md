# Django Web App Starter

## Supports
* HTTP
* Websockets

## How to Use
Make sure you have [Docker](http://docker.com) and [Docker Compose](https://docs.docker.com/compose/install/).

1. Run `docker-compose up`

Thats's it.  Docker will build the containers and bring up the services.  The web app will be available at `http://localhost`.

As of right now, if the startup script detects changes in a python file (*.py), then it will reload the Channels workers.
This means that you wont have to kill and restart the docker containers to see changes during development.
I do plan to add an environment variable that will disable the reload feature.

Make sure you visit both the [Django Documentation](https://docs.djangoproject.com/en/1.11/) and the [Channels Documentation](https://channels.readthedocs.io/en/latest/).

## Architecture

![Application Architecture](/static/img/django-channels.png?raw=true)


### Views
Add http views to `app/http/views/`.

Add http routes to `app/http/urls.py`.


Add WebSocket consumers to `app/ws/consumers`.
Add WebSocket routes to `app/ws/routing.py`.

*Examples are included in each file*
