from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from detector import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.detector_view, name='home'), # Homepage par apna AI chalega
]

# Photo upload show karne ke liye
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)