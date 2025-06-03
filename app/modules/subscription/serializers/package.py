from rest_framework import serializers
from app.modules.subscription.models.package import Package
from app.modules.general_module.serializers.admin_base_serializer import AdminBaseModelSerializer

class PackageSerializer(AdminBaseModelSerializer,serializers.ModelSerializer):        
    class Meta:
        model = Package
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']