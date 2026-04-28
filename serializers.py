from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'role', 'bio', 'avatar')
        read_only_fields = ('role',) # Users shouldn't be able to upgrade themselves
