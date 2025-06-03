from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from app.modules.subscription.models.package import Package
from app.modules.subscription.serializers.package import PackageSerializer
from app.core.mixins import AutoSetUserMixin

class PackageViewSet(AutoSetUserMixin,viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    authentication_classes = []
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = Package.objects.filter(subscriber=self.request.user.subscriber)
        return queryset