# coding=utf-8
from django.contrib import admin

from .models import Blog

admin.site.register(Blog)


class PostAdmin(admin.ModelAdmin):
    """在后台显示更详细的文章相关信息"""
    list_display = ['title', 'author', 'posted']
