from rest_framework import serializers
from app.modules.subscription.models.subscription import Subscription
from app.modules.subscription.serializers.package import PackageSerializer
from app.modules.general_module.serializers.admin_base_serializer import AdminBaseModelSerializer

class SubscriptionSerializer(AdminBaseModelSerializer,serializers.ModelSerializer):
    features = serializers.JSONField()
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

class SubscriptionNestedSerializer(AdminBaseModelSerializer,serializers.ModelSerializer):
    package = PackageSerializer()
    features = serializers.JSONField()
    # subscriber = SubscriberSerializer()
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']