from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import System
from django.contrib.auth.models import  User ,Group, Permission 




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # This hashes the password
        # Optionally, add to group logic can go here
        try:
            group = Group.objects.get(name="normal")
            user.groups.add(group)  # Add user to group
        except Group.DoesNotExist:
            raise serializers.ValidationError("Group does not exist.")
        return user

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken")
        return value




class SystemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=System.objects.all())]
    )
    class Meta:
        model = System
        fields = ['name', 'category']