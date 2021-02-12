from django.urls import path, include
from .views import index, result, downloads, file
import os 
from django.conf import settings
file_path = os.path.join(settings.MEDIA_ROOT, '<str:filename>/')
file_path = file_path[1:]
urlpatterns = [
    path('', index, name='index'),
    path('result/<int:amount>/', result, name='result'),
    path('downloads/', downloads, name='downloads'),
    path(file_path, file, name='file')
]