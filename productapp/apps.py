from django.apps import AppConfig

class ProductappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productapp'
    verbose_name = "2 จัดการสินค้า"  # เปลี่ยนเป็นชื่อที่ต้องการ
    
    def ready(self):
        import productapp.signals  # โหลด signals เมื่อแอปรัน

