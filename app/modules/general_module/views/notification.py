from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
# from rest_framework import status
from ..models.notification import Notification
from ..serializers.notification import NotificationSerializer, NotificationNestedSerializer
from app.core.mixins import AutoSetSubscriberMixin
from datetime import timedelta
from django.utils import timezone

# class NotificationViewSet(viewsets.ModelViewSet):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer

#     #override delete and send status 200 instead of 204
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_200_OK)

class NotificationViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = Notification.objects.all()  # Add this line
    serializer_class = NotificationSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return NotificationNestedSerializer
        return NotificationSerializer
    
    def get_queryset(self):
        #last_3_days = timezone.now() - timedelta(days=3)
        queryset = super().get_queryset()#.filter(created_at__gte=last_3_days)
        return queryset

    @action(detail=False, methods=['get'], url_path='unread')
    def unread_notifications(self, request):
        queryset = self.get_queryset().filter(is_read=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='unread-count')
    def unread_count(self, request):
        count = self.get_queryset().filter(is_read=False).count()
        return Response({'unread_count': count})

    @action(detail=False, methods=['post'], url_path='mark-all-read')
    def mark_all_read(self, request):
        self.get_queryset().filter(is_read=False).update(is_read=True)
        return Response({'status': 'all marked as read'})

    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all(self, request):
        self.get_queryset().delete()
        return Response({'status': 'all deleted'})

    @action(detail=True, methods=['post'], url_path='read')
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'status': 'marked as read'})