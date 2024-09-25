from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TestConnectionConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send_user_data()

    async def disconnect(self, close_code):
        pass  

    async def send_user_data(self):
        data = {
            "success": True
        }
        await self.send(text_data=json.dumps(data))

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        response = {
            'received_message': message
        }
        await self.send(text_data=json.dumps(response))
