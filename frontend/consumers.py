import json
from time import sleep
from channels.generic.websocket import WebsocketConsumer
from random import randint

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({'message': randint(0, 100)}))