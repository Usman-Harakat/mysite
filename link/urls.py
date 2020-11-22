from django.urls import path
from . import views

urlpatterns = [
    path('', views.link, name='link'),
    path('link2', views.link2, name='link2'),
]
