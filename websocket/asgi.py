import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import server.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')


application = ProtocolTypeRouter({
    
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            server.routing.websocket_urlpatterns
        )
    ),
})
