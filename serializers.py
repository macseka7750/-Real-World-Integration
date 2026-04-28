from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'author_username', 'title', 'content', 'is_premium', 'created_at')
