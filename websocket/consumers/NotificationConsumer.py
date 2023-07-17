import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from websocket.models import SocketChannel

class NotificationConsumer(AsyncWebsocketConsumer):
    connected_clients = set()

    async def connect(self):
        SocketChannel.get_instance().set_channel_name(self.channel_name)

        await self.accept()

        self.connected_clients.add(self)

    async def notify_user(self, event):
        response = {
            'notify': event['data']
        }

        await self.broadcast_message(json.dumps(response))

    async def broadcast_message(cls, message):
        await asyncio.gather(
            *(client.send_message(message) for client in cls.connected_clients)
        )

    async def send_message(self, message):
        await self.send(text_data=message)