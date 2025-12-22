from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ကိုယ့်ရဲ့ app က urls တွေကို ဒီမှာ include လုပ်ပေးရပါမယ်
    path('', include('app.urls')), 
]

# Development မှာ ပုံ (Images) တွေ ပေါ်လာအောင် လုပ်ဆောင်ခြင်း
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)