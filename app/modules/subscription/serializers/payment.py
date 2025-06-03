from rest_framework import serializers
from app.modules.subscription.models.payment import SubscriptionPayment
from app.modules.general_module.serializers.admin_base_serializer import AdminBaseModelSerializer

class SubscriptionPaymentSerializer(AdminBaseModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPayment
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']