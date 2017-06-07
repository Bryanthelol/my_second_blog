"""my_second_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from blog.api import BlogSet
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blog', BlogSet)

urlpatterns = [
    # 定义管理员页面的基础URL
    url(r'^admin/', include(admin.site.urls)),

    # 定义应用homepage的基础URL
    url(r'', include('homepage.urls', namespace='homepage')),

    # 定义应用blog的基础URL
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # 后台API显示页
    url(r'^api/', include(apiRouter.urls)),

]
