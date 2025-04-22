from django.db import models

class Message(models.Model):
    room = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)  # ✅ อนุญาตให้ content เป็นค่าว่าง
    file = models.FileField(upload_to="chat_files/", blank=True, null=True)  # ✅ รองรับไฟล์แนบ (รูปภาพ, PDF, ZIP ฯลฯ)
    is_image = models.BooleanField(default=False)  # ✅ ระบุว่าไฟล์เป็นรูปภาพหรือไม่
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.content or ('📷 Image' if self.is_image else '📎 File Attached')} ({self.timestamp})"
