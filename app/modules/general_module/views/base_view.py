from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorized

class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAuthorized]