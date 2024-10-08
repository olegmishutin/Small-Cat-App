from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websockets

asgi = get_asgi_application()

application = ProtocolTypeRouter({
    'http': asgi,
    "websocket": AuthMiddlewareStack(websockets),
})