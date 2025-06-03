from rest_framework import viewsets
from rest_framework.response import Response
from app.modules.subscription.models.subscriber import Subscriber
from app.modules.subscription.serializers.subscriber import SubscriberSerializer,SubscriberNestedSerializer
from django.db import transaction
from app.modules.general_module.models.document import Document
from app.core.mixins import AutoSetUserMixin

class SubscriberViewSet(AutoSetUserMixin,viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:  # For GET requests
            return SubscriberNestedSerializer
        return SubscriberSerializer  # For POST/PUT requests
    
    def create(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                with transaction.atomic():  # ✅ Ensures all-or-nothing save                    
                    subscriber = serializer.save()

                    for key in request.FILES:
                        document = Document.objects.create(
                            parent_type='subscriber',
                            parent_id=subscriber.id,
                            document_name='logo', 
                            document_file=request.FILES[key]
                        )

                    return Response(SubscriberNestedSerializer(subscriber).data, status=201)
            except Exception as e:
                transaction.rollback()  # Explicitly rollback on failure
                return Response({"error": str(e)}, status=400)
            
        return Response(serializer.errors, status=400)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubscriberSerializer(instance, data=request.data)
        
        if serializer.is_valid():
            try:
                with transaction.atomic():  # ✅ Ensures all-or-nothing save                    
                    subscriber = serializer.save()
                                    
                    for key in request.FILES:
                        try:
                            document = Document.objects.get(
                                parent_type='subscriber',
                                parent_id=subscriber.id
                            )
                            document.delete()
                        except Document.DoesNotExist:
                            pass
                
                        document = Document.objects.create(
                            parent_type='subscriber',
                            parent_id=subscriber.id,
                            document_name='logo', 
                            document_file=request.FILES[key],
                            subscriber=subscriber
                        )

                    return Response(SubscriberNestedSerializer(subscriber).data, status=201)
            except Exception as e:
                transaction.rollback()  # Explicitly rollback on failure
                return Response({"error": str(e)}, status=400)
            
        return Response(serializer.errors, status=400)