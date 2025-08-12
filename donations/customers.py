import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DonationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.campaign_id = self.scope['url_route']['kwargs']['campaign_id']
        self.room_group_name = f"campaign_{self.campaign_id}"
        
        # Join group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'donation_update',
                'message': data['message']
            }
        )

    async def donation_update(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
