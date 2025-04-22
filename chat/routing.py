from django.urls import re_path
from .consumers import ChatConsumer
from . import consumers


websocket_urlpatterns = [
    # รูปแบบ URL สามารถกำหนดได้ตามที่คุณต้องการ
    re_path(r'^ws/chat/(?P<room_name>[\w-]+)/$', consumers.ChatConsumer.as_asgi()),
]