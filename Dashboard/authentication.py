from rest_framework.authentication import SessionAuthentication 
  
class CsrfExemptSessionAuthentication(SessionAuthentication): # ✅ ปิด CSRF ตรวจสอบ 
    def enforce_csrf(self, request):
        return  # ✅ ปิด CSRF ตรวจสอบ 