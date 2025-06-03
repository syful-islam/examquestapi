from rest_framework import serializers
from app.modules.subscription.models.subscriber import Subscriber
from app.modules.subscription.models.subscription import Subscription
from app.modules.subscription.serializers.subscription import SubscriptionNestedSerializer
from app.modules.general_module.models.document import Document
from app.modules.general_module.serializers.document import DocumentSerializer
from app.modules.general_module.serializers.admin_base_serializer import AdminBaseModelSerializer

class SubscriberSerializer(AdminBaseModelSerializer,serializers.ModelSerializer):  
    class Meta:
        model = Subscriber
        fields = '__all__'
        extra_kwargs = {
            'subscription_id': {'read_only': True},
        }
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

class SubscriberNestedSerializer(AdminBaseModelSerializer,serializers.ModelSerializer):
    documents = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()
    
    class Meta:
        model = Subscriber
        fields = '__all__'
        extra_kwargs = {
            'subscription_id': {'read_only': True},
        }
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    def get_documents(self, obj):
        """Retrieve Documents for the contract using parent_id."""
        documents = Document.objects.filter(parent_type="subscriber", parent_id=obj.id)
        return DocumentSerializer(documents, many=True).data
    
    def get_subscription(self, obj):
        """Retrieve SLAs for the contract using parent_id."""
        print("Subscription id ",obj.subscription_id)
        subscription = Subscription.objects.filter(id=obj.subscription_id).first()
        if not subscription:
            return None
        
        return SubscriptionNestedSerializer(subscription).data
