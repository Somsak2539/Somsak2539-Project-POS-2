from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Product1

#เอาไว้สำหรับการลบเมื่อมีการลบก็จะทำการลบออกจาก severอีกด้วย
@receiver(post_delete, sender=Product1)
def delete_product_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)  # ลบไฟล์จริงออกจากเซิร์ฟเวอร์
