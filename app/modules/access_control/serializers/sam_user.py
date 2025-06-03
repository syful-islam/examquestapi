from rest_framework import serializers
from ....models import SAMUser
from app.modules.subscription.serializers.subscriber import SubscriberNestedSerializer
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer

class SAMUserSerializer(BaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = SAMUser
        fields = ('id', 'email','full_name', 'mobile_no','password', 'subscriber','is_admin')  # Include 'password' in fields
        extra_kwargs = {
            'is_admin': {'read_only': True},
            'password': {'write_only': True, "required": False}  # Password should be write-only, not returned in responses
        }
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    def create(self, validated_data):
        if 'password' not in validated_data:
            raise serializers.ValidationError({'password': 'This field is required.'})
        
        if 'subscriber' not in validated_data:
            raise serializers.ValidationError({'subscriber': 'This field is required.'})
        
        # Pop and hash the password before saving
        password = validated_data.pop('password')
        
        user = SAMUser.objects.create_user(**validated_data, password=password)
        return user

    def update(self, instance, validated_data):
        # Remove password from validated_data if not provided
        validated_data.pop('password', None)  
        return super().update(instance, validated_data)

class SAMUserNestedSerializer(BaseModelSerializer,serializers.ModelSerializer):
    subscriber=SubscriberNestedSerializer()

    class Meta:
        model = SAMUser
        fields = ('id', 'email','full_name', 'mobile_no','password', 'subscriber','is_admin')  # Include 'password' in fields
        extra_kwargs = {
            'is_admin': {'read_only': True},
            'password': {'write_only': True, "required": False}  # Password should be write-only, not returned in responses
        }
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']