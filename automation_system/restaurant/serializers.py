from core.models import System
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import MenuItem







class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "id", "system", "name", "description", "price", "is_available",
            "category", "image", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at", "system"]

    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2, allow_null=True)
    image = serializers.ImageField(required=False, allow_null=True)

    def create(self, validated_data):
        request = self.context["request"]
        system_id = self.context["view"].kwargs.get("system_id")

        # Ensure system exists and belongs to the current user
        try:
            system = System.objects.get(id=system_id, owner=request.user)
        except System.DoesNotExist:
            raise serializers.ValidationError("Invalid system or unauthorized access.")

        validated_data["system"] = system
        return super().create(validated_data)








# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = [
#             "id",
#             "system",
#             "name",
#             "description",  # This field will be optional
#             "price",        # This field will be optional
#             "is_available", # Default to True if not provided
#             "category",
#             "image",        # This field will also be optional
#             "created_at",
#             "updated_at",
#         ]
#         read_only_fields = ["id", "created_at", "updated_at", "system"]


#     # Making specific fields optional
#     description = serializers.CharField(required=False, allow_blank=True)# Optional field
#     price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)  # Optional field
#     image = serializers.ImageField(required=False, allow_null=True)  # Optional field

#     def create(self, validated_data):
#         if 'is_available' not in validated_data:
#             validated_data['is_available'] = True
#         return super().create(validated_data)
    
#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)

#     def validate_system(self, value):
#         # Get the user from the context (such as from the request)
#         user = self.context['request'].user

#         # Check if the System exists and belongs to the user
#         try:
#             system = System.objects.get(id=value.id, owner=user)
#         except System.DoesNotExist:
#             raise serializers.ValidationError("The system does not exist or does not belong to you.")

#         return value