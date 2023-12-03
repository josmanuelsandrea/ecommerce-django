from rest_framework import serializers
from users.models import User
from uuid import uuid4

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        username = validated_data.pop('username', uuid4())
        instance = self.Meta.model(username=username, **validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name']

class UserInfoNeeded(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)