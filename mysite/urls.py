
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from mysite.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.DocumentCreateView.as_view(), name='home'),
]
