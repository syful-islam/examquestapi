from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from app.modules.utils.email_utility import EmailService
from app.modules.utils.otp_utility import OTPService
from ..serializers.otp import OTPSerializer, OTPValidateSerializer
from django.utils import timezone
from app.modules.student_management.models import SAMUser
from app.modules.access_control.serializers.sam_user import SAMUserSerializer

class SendOTPView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']            
            
            try:
                user = SAMUser.objects.get(email=email)                
            except SAMUser().DoesNotExist:
                return  Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
            otp_service = OTPService()
            email_service = EmailService()
            
            otp = otp_service.create_otp(email)
            success = email_service.send_otp_email(email, otp, "User")  # Replace "User" with actual name if available
            
            if success:
                return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ValidateOTPView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = OTPValidateSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = SAMUser.objects.get(email=email)                
            except SAMUser().DoesNotExist:
                return  Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
            otp_service = OTPService()
            if otp_service.validate_otp(email, otp):
                if user.email_verified_at is None:
                    user.email_verified_at = timezone.now()
                    user.save()
                
                # return Response({"message": "OTP validated successfully"}, status=status.HTTP_200_OK)
                return Response(SAMUserSerializer(user).data, status=status.HTTP_200_OK)
            return Response({"error": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendNotificationView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        email_service = EmailService()
        success = email_service.send_notification(
            request.data.get('email'),
            request.data.get('message'),
            request.data.get('user_name', 'User')
        )
        if success:
            return Response({"message": "Notification sent successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Failed to send notification"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)