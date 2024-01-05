from django.contrib import admin
from django.urls import path, include
from django.urls import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path("__reload__/", include("django_browser_reload.urls"))
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
