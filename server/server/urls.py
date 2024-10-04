from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/', include([
        path('', include('cats.urls')),
        path('', include('authentication.urls')),
    ])),
    path('admin/', admin.site.urls),
    path('', include(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)))
]
