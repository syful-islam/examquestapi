from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status, permissions
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password, make_password
from app.modules.student_management.models import SAMUser
from ..serializers.login import LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
from app.modules.access_control.serializers.sam_user import SAMUserSerializer, SAMUserNestedSerializer
from ..services.auth_service import AuthService
from app.modules.utils.otp_utility import OTPService
from app.modules.subscription.models.subscriber import Subscriber
from app.modules.subscription.models.subscription import Subscription
from app.modules.subscription.models.package import Package
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from rest_framework.permissions import AllowAny
import json
from rest_framework.parsers import MultiPartParser, FormParser
from app.core.logger import log

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()

        try:
            organization = request.data.get('organization')
            if not organization:
                raise AuthenticationFailed("Organization is required")
            
            package_id = request.data.get('package')
            package = Package.objects.filter(id=package_id).first()
            if not package:
                raise AuthenticationFailed("Package is required")
            
            features = request.data.get('features', {})
            log.debug(f"features Data: {features}")         
            # sam = features.get('sam')
            # rfp = features.get('rfp')
            # cm = features.get('cm')

            # features_keys = ['sam', 'rfp', 'cm']
            # features = {key: request.POST.get(f'features[{key}]') for key in features_keys}

            if not any(features.values()):
                raise AuthenticationFailed("Features are required")
            
            email = request.data.get('email')        
            if not email:
                raise AuthenticationFailed("Email is required")
        
            subscriber = Subscriber.objects.filter(name=organization).first()
            if subscriber:
                raise AuthenticationFailed("You are already registered. Please contact your administrator")
            
            user = SAMUser.objects.get(email=email)
            if user.email_verified_at:
                raise AuthenticationFailed("You are already registered")
            else:
                return Response(SAMUserNestedSerializer(user).data, status=status.HTTP_201_CREATED)
        except Package().DoesNotExist:
                    raise AuthenticationFailed("Package is required")                
        except SAMUser().DoesNotExist:            
            serializer = SAMUserSerializer(data=data)

            if serializer.is_valid():
                try:
                    with transaction.atomic():
                                
                        subscriber = Subscriber.objects.create(
                            name=organization,
                            address_line1 = request.data.get('address'),
                            contact_email = email,
                            contact_phone = request.data.get('mobile_no'),
                            status = "Active")
                        subscriber.save()
                        print("subscriber created", subscriber.id)

                        serializer.validated_data['subscriber'] = subscriber
                        user = serializer.save()
                        user.is_admin = True  # or some condition
                        user.save()
                        print("user created", user.full_name)

                        subscription=Subscription.objects.create(
                            subscriber = subscriber,
                            package = package,
                            features = features,
                            start_date=timezone.now(),  # Use timezone-aware datetime
                            end_date=timezone.now() + relativedelta(years=1),  # Use timezone-aware datetime
                            renewal_date=timezone.now() + relativedelta(years=1)  # Use timezone-aware datetime
                        )
                        subscription.save()
                        print("subscription created", subscription.id)
                        #update subscriber with with latest subscription id
                        subscriber.subscription_id = subscription.id
                        subscriber.save()
                        print("subscriber update", subscriber.id)
                        # return Response(serializer.data, status=status.HTTP_201_CREATED)
                        return Response(SAMUserNestedSerializer(user).data, status=status.HTTP_201_CREATED)
                except Exception as e:
                    transaction.rollback()  # Explicitly rollback on failure
                    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            raise AuthenticationFailed("email and password are required")
        
        try:
            user = SAMUser.objects.get(email=email)

            if user.email_verified_at is None:
                raise AuthenticationFailed("Email not verified")
            
        except SAMUser().DoesNotExist:
            raise AuthenticationFailed("User not found")

        if not check_password(password, user.password):
            raise AuthenticationFailed("Invalid credentials")
        
        access_token = AuthService.create_access_token(user, 'ProcureLogic')

        response_data = SAMUserNestedSerializer(user).data
        response_data['access_token'] = access_token.token
        response_data['expires_in'] = access_token.expires
        return Response(response_data, status=status.HTTP_200_OK)
    
        # serializer = LoginSerializer(data=request.data)
        # if serializer.is_valid():
        #     user = serializer.validated_data
        #     # access_token = AuthService.create_access_token(user, 'evchargingapp')
        #     # return Response({
        #     #     'access_token': access_token.token,
        #     #     'expires_in': access_token.expires
        #     # }, status=status.HTTP_200_OK)
        #     #reponse user details
        #     return Response(EVUserSerializer(user).data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():            
            try:
                user = SAMUser.objects.get(email=email)
            except SAMUser().DoesNotExist:
                raise AuthenticationFailed("User not found")
            
            if not check_password(serializer.validated_data["old_password"], user.password):           
                return Response({"error": "Incorrect old password"}, status=status.HTTP_400_BAD_REQUEST)

            user.password = make_password(serializer.validated_data["new_password"])
            user.save()
            return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            user = SAMUser.objects.filter(email=email).first()
            if user:
                # Simulating email sending (replace with actual logic)
                send_mail("Password Reset Request", "Reset your password here.", "admin@example.com", [email])
            return Response({"message": "If the email exists, a reset link has been sent."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():            
            try:
                user = SAMUser.objects.get(email=email)
            except SAMUser().DoesNotExist:
                raise AuthenticationFailed("User not found")

            otp_service = OTPService()
            if otp_service.otp_validated(email):
                user.password = make_password(serializer.validated_data["new_password"])
                user.save()
                return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "OTP validation required"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)