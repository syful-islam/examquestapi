from rest_framework.exceptions import PermissionDenied
from app.core.logger import log

class AutoSetSubscriberMixin:
    """
    Automatically injects request.user.subscriber, request.user into serializer.save() during create and update operations.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated or not hasattr(self.request.user, 'subscriber'):
            raise PermissionDenied("User must be authenticated to access.")
        return super().get_queryset().filter(subscriber=self.request.user.subscriber)
            
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated or not hasattr(self.request.user, 'subscriber'):
            raise PermissionDenied("User must be authenticated to access.")
        serializer.save(subscriber=self.request.user.subscriber, created_by=self.request.user.id)

    def perform_update(self, serializer):
        if not self.request.user.is_authenticated or not hasattr(self.request.user, 'subscriber'):
            raise PermissionDenied("User must be authenticated to access.")
        serializer.save(subscriber=self.request.user.subscriber, updated_by=self.request.user.id)


class AutoSetUserMixin:
    """
    Automatically injects request.user.subscriber, request.user into serializer.save() during create and update operations.
    """
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("User must be authenticated to access.")
        serializer.save(created_by=self.request.user.id)

    def perform_update(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("User must be authenticated to access.")
        serializer.save(updated_by=self.request.user.id)