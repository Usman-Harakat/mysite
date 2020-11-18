from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('link.urls')),
    path('dob/', include('link.urls')),
    path('admin/', admin.site.urls),
]
