from rest_framework import viewsets
from app.modules.subscription.models.subscription import Subscription
from app.modules.subscription.serializers.subscription import SubscriptionSerializer, SubscriptionNestedSerializer
from app.core.mixins import AutoSetUserMixin

class SubscriptionViewSet(AutoSetUserMixin,viewsets.ModelViewSet):
    queryset = Subscription.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return SubscriptionNestedSerializer
        return SubscriptionSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        queryset = Subscription.objects.filter(subscriber=self.request.user.subscriber)
        return queryset