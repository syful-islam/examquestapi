from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from ....models import SAMUser
from ..serializers.sam_user import SAMUserSerializer, SAMUserNestedSerializer
from app.modules.auth.services.auth_service import AuthService
from app.core.mixins import AutoSetSubscriberMixin
from app.core.logger import log

class SAMUserViewSet(AutoSetSubscriberMixin,viewsets.ModelViewSet):
    queryset = SAMUser.objects.all()
    serializer_class = SAMUserSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # For GET requests
            return SAMUserNestedSerializer
        return SAMUserSerializer  # For POST/PUT requests
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def create(self, request, *args, **kwargs):
        # token = request.headers.get("Authorization", "").replace("Bearer ", "")
        # if not token:
        #     return Response({"error": "Token required"}, status=400)

        try:
            # app_user = AuthService.get_user_by_token(token)
            # if not app_user:
            #     return Response({"error": "Invalid token"}, status=400)
            
            # print("app_user", app_user.__dict__)
            data = request.data.copy()
            # data['subscriber'] = app_user.subscriber.id
            serializer = SAMUserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            #update user and set is_admin=True
            
            # user = serializer.instance
            # if 
            # user.is_admin = True
            # user.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)                        
    
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
                
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            log.error(f"Error: {str(e)}")
            related_objects = e.protected_objects  # List of objects causing the error
        
            # Extract model names of related objects
            related_models = set(obj._meta.verbose_name for obj in related_objects)
            related_models_str = ", ".join(related_models)

            return JsonResponse({
                "error": f"Cannot delete software because related {related_models_str} exist."
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log.error(f"Error: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)