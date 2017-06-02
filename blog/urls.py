from django.conf.urls import url

from . import views

# 告诉 Django 这个URL文件用于这个应用
app_name = 'blog'

urlpatterns = [
    # 博客列表页
    url(r'^$', views.blog_lists, name='blog_lists'),

    # 博客详情页
    url(r'^detail/(?P<my_args>\d+)/$', views.blog_detail, name='blog_detail'),
]
