from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PremiumContentPermission(permissions.BasePermission):
    """
    Custom permission to only allow Premium users to see premium posts.
    """
    def has_object_permission(self, request, view, obj):
        if obj.is_premium:
            return request.user.role in ['PREMIUM', 'ADMIN', 'MODERATOR']
        return True

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, PremiumContentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
