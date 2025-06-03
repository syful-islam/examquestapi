from rest_framework import serializers
from ..models.notification import Notification
from app.modules.access_control.serializers.sam_user import SAMUserSerializer
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer

class NotificationSerializer(BaseModelSerializer,serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name', read_only=True)    
    
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by'] #'user',

class NotificationNestedSerializer(BaseModelSerializer,serializers.ModelSerializer):
    user = SAMUserSerializer()
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by'] #'user',