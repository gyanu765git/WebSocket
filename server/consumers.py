from channels.generic.websocket import AsyncWebsocketConsumer

import logging
logger = logging.getLogger(__name__)

class TestConnectionConsumer(AsyncWebsocketConsumer):

    async def connect(self):
            await self.send_user_data()
            await self.accept()

    async def disconnect(self):
        pass  

    async def send_user_data(self):
         print("connected.....")
        

