from rest_framework import viewsets
from app.modules.subscription.models.payment import SubscriptionPayment
from app.modules.subscription.serializers.payment import SubscriptionPaymentSerializer
from app.core.mixins import AutoSetUserMixin

class SubscriptionPaymentViewSet(AutoSetUserMixin,viewsets.ModelViewSet):
    queryset = SubscriptionPayment.objects.all()
    serializer_class = SubscriptionPaymentSerializer

    def get_queryset(self):
        queryset = SubscriptionPayment.objects.filter(subscriber=self.request.user.subscriber)
        return queryset