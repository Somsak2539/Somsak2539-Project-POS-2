"""
Django settings for shoping project.
"""

from pathlib import Path
import os

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ ตั้งค่า Static & Media
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# ✅ ตั้งค่า Secret Key
SECRET_KEY = 'django-insecure-t=278n2b3dn-ke#e&z_s0(kw8=gi47bcy50xx!ndy17peynb03'
DEBUG = True

# ✅ ตั้งค่า Host ที่อนุญาต
ALLOWED_HOSTS = ["*", "127.0.0.1","[2001:44c8:4518:d5e5:50fb:df16:7172:726f]","0.0.0.0","172.20.10.5",  'somsaksonngai.duckdns.org', '182.232.184.157','somsaksonngai.site','localhost:8080',  ]

# ✅ ติดตั้งแอปที่ต้องใช้
INSTALLED_APPS = [
    "pwa",
    "django_cleanup.apps.CleanupConfig", 
    "daphne",
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "productapp",
    "userapp",
    "cartapp",
    "orderapp",
    "Dashboard",
    "DashboardUser",
    "chat",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "rangefilter",'django.contrib.humanize',
]




PWA_APP_NAME = 'My WebApp'
PWA_APP_DESCRIPTION = "แอปของแบงค์สุดน่ารัก"
PWA_APP_THEME_COLOR = '#FFFFFF'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_SCOPE = '/'
PWA_APP_START_URL = '/'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icon-512x512.png',
        'sizes': '512x512'
    }
]












# ✅ Channels (WebSocket)
ASGI_APPLICATION = "shoping.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}


CSP_SCRIPT_SRC = (
    "'self'", 
    'https://unpkg.com', 
    'https://somsaksonngai.site'
)


# ✅ Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 1,
}

# ✅ Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # ✅ CORS ต้องอยู่ด้านบนสุด!
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #"django.middleware.csrf.CsrfViewMiddleware", # ✅ CORS ลองปิดดู clean ต้องส่ง crfs token ไปเพราะยังไม่ถูกส่งใช้สำหรับการทดสอบเท่านั้น 
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
]



# ✅ อนุญาตให้ใช้ CORS (Cross-Origin)

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    "content-type",
    "X-CSRFToken",
   
]

# ✅ ปรับค่า CSRF Cookie
#CSRF_USE_SESSIONS = True  # ❌ ปิดการใช้ CSRF Token ผ่าน Session

#CSRF_COOKIE_HTTPONLY = False  # ✅ อนุญาตให้ JavaScript อ่าน Cookie CSRF
#CSRF_COOKIE_SECURE = False  # ✅ ใช้ HTTPS เท่านั้น ถ้าไม่ได้ใช้ HTTPS ต้องตั้งเป็น False


#CSRF_COOKIE_SAMESITE = "None"  # ✅ อนุญาตให้ใช้งานข้าม Origin
#SESSION_COOKIE_SECURE = True  # ✅ ปิดเพื่อให้ส่ง Session Cookie ได้
#SESSION_COOKIE_SAMESITE = "None"  # ✅ อนุญาตให้ส่ง Session Cookie ข้าม Origin

CORS_ALLOWED_ORIGINS = [
    'https://somsaksonngai.site',
    "http://127.0.0.1:8080",
    "https://localhost:8080",
    "http://localhost:8080",
    "http://[2001:44c8:44c5:8e4c:8d1:e48a:2672:947c]:8080",
    "http://[2001:44c8:48f3:2772:dc0d:bdd0:30a7:3266]:8080", 
   # "http://192.168.40.250:8080",# Ip เครืองตัวเอง
    

]

# ✅ อนุญาตให้ CSRF ทำงานกับไอพีเซิร์ฟเวอร์
CSRF_TRUSTED_ORIGINS = [
    
    "http://127.0.0.1:8080",#ตัวนี้เป็น http ธรรมดา
    "http://localhost:8080",#ตัวนี้เป็น http ธรรมดา
    "http://[2001:44c8:44c5:8e4c:8d1:e48a:2672:947c]:8080", #ตัวนี้เป็น http ธรรมดา
    "https://localhost:8080",
    "https://127.0.0.1:8080",#ตัวนี้เป็น http ธรรมดา
    "https://localhost:8080",#ตัวนี้เป็น http ธรรมดา
    "https://[2001:44c8:48f3:2772:c93a:186:3b11:2ab6]:8080",  #ตัวนี้เป็น https 
    'https://somsaksonngai.site',
    "https://[2001:44c8:48f3:2772:9585:8354:93a2:c187]:8080",
    #"http://192.168.40.250:8080",  # Ip เครืองตัวเอง
]

# ✅ ปิด `SECURE_CROSS_ORIGIN_OPENER_POLICY`
SECURE_CROSS_ORIGIN_OPENER_POLICY = None



# ✅ URL Configuration
ROOT_URLCONF = "shoping.urls"

# ✅ Templates Configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        
        'DIRS': [os.path.join(BASE_DIR, 'DashboardUser/templates')], 
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ✅ WSGI
WSGI_APPLICATION = "shoping.wsgi.application"

# ✅ Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# settings.py
VIEW_SITE_URL = "https://somsaksonngai.site/indexDashboardUser/"  # หรือดึงจาก Environment Variable

# ✅ Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Language & TimeZone
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Bangkok"
USE_I18N = True
USE_TZ = True

# ✅ Default Auto Field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = '/login_cover/'  # กำหนด URL ที่ให้ redirect ไปหน้า login
