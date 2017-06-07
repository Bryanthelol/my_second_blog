from blog.models import Blog
from django.contrib.auth.models import User
from rest_framework import permissions, serializers, viewsets


class BlogSerializer(serializers.ModelSerializer):
    author = User

    class Meta:
        model = Blog
        fields = ('title', 'author', 'body', 'slug', 'id')


class BlogSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
