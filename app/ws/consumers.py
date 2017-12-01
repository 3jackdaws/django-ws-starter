
from channels.generic.websockets import JsonWebsocketConsumer
from channels.message import Message
from django.contrib.auth.models import User
from channels import Group, Channel


import json
import os



class EchoWSConsumer(JsonWebsocketConsumer):

    def connection_groups(self, **kwargs):
        return ('groupname')

    def connect(self, message:Message, **kwargs):
        self.send(json.dumps({'accept': True}))


    def receive(self, text=None, bytes=None, **kwargs):

        self.send()




