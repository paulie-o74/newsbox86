from django.contrib import admin
from django.urls import path, include
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls'))
]

handler404 = 'newsbox86.views.handler404'
