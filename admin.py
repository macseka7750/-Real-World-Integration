from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_premium', 'created_at')
    list_filter = ('is_premium', 'created_at')
    search_fields = ('title', 'content')
