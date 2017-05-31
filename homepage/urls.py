"""这个文件定义应用homepage的具体URL模式"""

from django.conf.urls import url

from . import views

# 告诉 Django 这个URL文件用于这个应用
app_name = 'homepage'

urlpatterns = [
    # 着陆页
    url(r'^$', views.index, name='index'),
]
