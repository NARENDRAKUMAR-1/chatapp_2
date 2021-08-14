"""
ASGI config for mysite_1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

import chat_1.routing  # take note
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_1.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)

    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_1.routing.websocket_urlpatterns
        )
    ),
})
# ..................................................................................................

# However if you open a second browser tab to the same room page at http://127.0.0.1:8000/chat/lobby/ and type in a message, the message will not appear in the first tab. For that to work, we need to have multiple instances of the same ChatConsumer be able to talk to each other. Channels provides a channel layer abstraction that enables this kind of communication between consumers


# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.conf.urls import url
# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite_1.settings")
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# from chat_1.consumers import AdminChatConsumer, PublicChatConsumer

# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,

#     # WebSocket chat handler
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             url(r"^chat_1/admin/$", AdminChatConsumer.as_asgi()),
#             url(r"^chat_1/$", PublicChatConsumer.as_asgi()),
#         ])
#     ),
# })