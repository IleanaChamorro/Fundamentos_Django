from django.contrib import admin
from django.urls import path, include
from posts.views import dummy_view, status_code_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', status_code_view, name='home'),
    path('entries', include('posts.urls', namespace='entries'))
]

handler404 = 'posts.views.status_code_view'