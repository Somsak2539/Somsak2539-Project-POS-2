from django.shortcuts import render,redirect
from .models import Message

def chat_room(request, room_name=None):
    if not room_name:  # ตรวจสอบว่ามี room_name หรือไม่
        return redirect("/")  # หรือ return HttpResponse("Error: Room name is required")
    
    messages = Message.objects.filter(room=room_name).order_by("timestamp")
    return render(request, "chat.html", {
        "room_name": room_name,
        "messages": messages #ส่งข้อมูลความไปยังtemplate 
    })