from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/donations/(?P<campaign_id>\d+)/$', consumers.DonationConsumer.as_asgi()),
]
