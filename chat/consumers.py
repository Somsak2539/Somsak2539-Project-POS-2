import os
import json
import base64
import mimetypes
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from datetime import datetime
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()

            # ✅ ดึงประวัติแชทจากฐานข้อมูล (ต้องอยู่ใน `else:`)
            messages = await self.get_chat_history()
            await self.send(text_data=json.dumps({
                "type": "chat_history",
                "messages": messages
            }))

    async def get_chat_history(self):
        """✅ ฟังก์ชันดึงประวัติแชทจากฐานข้อมูล"""
        messages = await sync_to_async(lambda: list(Message.objects.filter(room=self.room_name).order_by("timestamp")))()
        return [{"sender": msg.username, "message": msg.content, "timestamp": msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")} for msg in messages]


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender = self.scope["user"].username

        # ✅ ตรวจสอบว่า JSON มี 'file' หรือ 'message' หรือไม่
        if "file" in data:
            file_data = data["file"]
            file_name = data["filename"]
            file_type = data["filetype"]

            # แปลง Base64 เป็นไฟล์และเช็คว่าเป็นภาพหรือไม่
            saved_file_path, is_image = await self.save_file(file_data, file_name, file_type)

            # บันทึกข้อความลงฐานข้อมูล
            await self.save_message(self.room_name, sender, None, saved_file_path, is_image)

            # ส่งข้อมูลไปยัง WebSocket
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": None,
                    "file": saved_file_path,
                    "is_image": is_image,
                    "sender": sender,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                },
            )

        elif "message" in data:  # ✅ ตรวจสอบว่ามี message ก่อนอ่านค่า
            message = data["message"]
            await self.save_message(self.room_name, sender, message, None, False)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "file": None,
                    "is_image": False,
                    "sender": sender,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                },
            )

        else:
            print("⚠️ Error: JSON ไม่มี 'message' หรือ 'file'")

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "file": event["file"],
            "is_image": event["is_image"],
            "sender": event["sender"],
            "timestamp": event["timestamp"],
        }))

    @sync_to_async
    def save_message(self, room, sender, message, file_name, is_image):
        if not message and not file_name:  # ✅ ป้องกันการบันทึกข้อความว่าง
            return  
        Message.objects.create(room=room, username=sender, content=message or "", file=file_name, is_image=is_image)

    @sync_to_async
    def save_file(self, file_data, file_name, file_type):
        file_path = os.path.join(settings.MEDIA_ROOT, "chat_files", file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        file_binary = base64.b64decode(file_data)
        with open(file_path, "wb") as f:
              f.write(file_binary)

        return f"/{file_name}", file_type.startswith("image/")

