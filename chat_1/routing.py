from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat_1/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),

    # here too chat_1 as the app name

    # We call the as_asgi() classmethod in order to ge
    # t an ASGI application that will instantiate an instance of our consumer for each user-connection. 
    # This is similar to Django’s as_view(), which plays the same role for per-request Django view instances.

]