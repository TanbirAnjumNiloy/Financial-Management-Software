from django.contrib import admin
from django.urls import path, include
from login import views
from django.conf import settings  # Import the settings module
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('setup.urls')),
    path('', include('account.urls')),
    path('', include('analysis.urls')),
    path('', include('control.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
