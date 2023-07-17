import json
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http.response import HttpResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from websocket.models import SocketChannel

# Create your views here.

@async_to_sync
@require_POST
async def send_message(request):
    body_request = json.loads(request.body)

    channel_layer = get_channel_layer()
    channel_name = SocketChannel.get_instance().channel_name

    await channel_layer.send(channel_name, { 'type': 'notify_user', 'data': body_request })

    return HttpResponse(json.dumps({ "message": "mensaje enviado correctamente" }))

