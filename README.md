# Django Web App Starter

## Features
* Fully featured web application boilerplate
* Is Django
* Supports WebSockets
* Automatic code reloading on changes (for development)
* Supports Docker


## How to Use
Make sure you have [Docker](http://docker.com) and [Docker Compose](https://docs.docker.com/compose/install/).

1. Run `docker-compose up`

Thats's it.  Docker will build the containers and bring up the services.  The web app will be available at `http://localhost`.

As of right now, if the startup script detects changes in a python file (*.py), then it will reload the Channels workers.
This means that you wont have to kill and restart the docker containers to see changes during development.
I do plan to add an environment variable that will disable the reload feature.

Make sure you visit both the [Django Documentation](https://docs.djangoproject.com/en/1.11/) and the [Channels Documentation](https://channels.readthedocs.io/en/latest/).

### Without Docker
If you *really* don't want to install Docker, you can manually setup your all your own component services by running all the commands in the Dockerfile.

### Adding Pages
This is based on Django.  To add new pages/content, add a HTTP view in `app/http/views/`, add a template in `templates/app/` and link the two.
Look in `app/views/common.py` for the index view, that should give you a general idea of how to add content.

Websocket code can be added to `app/ws/consumers.py`.  View app.ws.consumers.EchoWSConsumer for example code.
Websocket "Views" must be routed in a similar way to HTTP views.  The WS routing file is app/ws/routing.py.


## Architecture

![Application Architecture](/static/img/django-channels.png?raw=true)

\* *Workers can handle both HTTP and WS tasks at the same time*






# Contributing
Sure, just fork and submit a pull request and a reason for changes.

# License
Copyright 2017, Ian Murphy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

