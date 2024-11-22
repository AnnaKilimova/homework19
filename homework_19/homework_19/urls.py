from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('min_django_app/', include('min_django_app.urls')),
]
