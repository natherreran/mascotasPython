from django.conf.urls import include, url
from .views import index, mascota_view

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nueva-mascota$', mascota_view, name='mascota_crear'),
]