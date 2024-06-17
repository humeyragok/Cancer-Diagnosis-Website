from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.home,name = 'index'),
    path('test',views.upload_image,name= "test"),
    path('result',views.upload_image,name= "result"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)