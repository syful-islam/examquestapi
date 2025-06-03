import random
import string
from django.utils import timezone  # Ensure this is imported
from datetime import datetime, timedelta
from django.conf import settings
from app.modules.auth.models.otp import OTP

class OTPService:
    def __init__(self):
        self.otp_length = getattr(settings, 'OTP_LENGTH', 6)
        self.expiry_minutes = getattr(settings, 'OTP_EXPIRY_MINUTES', 30)

    def generate_otp(self):
        characters = string.digits
        return ''.join(random.choice(characters) for _ in range(self.otp_length))

    def create_otp(self, email):
        otp = self.generate_otp()
        expiry_time = timezone.now() + timedelta(minutes=self.expiry_minutes)
        
        # Delete any existing OTP for this user
        OTP.objects.filter(email=email).delete()
        
        # Create new OTP
        OTP.objects.create(
            email=email,
            otp=otp,
            expiry_time=expiry_time
        )
        return otp

    def validate_otp(self, email, otp):
        try:
            otp_record = OTP.objects.get(email=email, otp=otp)
            if otp_record.expiry_time >= timezone.now():  # Fix: Use timezone.now()
                # otp_record.delete()  # OTP is one-time use
                otp_record.verified_at = timezone.now()
                otp_record.save()
                return True
            else:
                otp_record.delete()  # Delete expired OTP
                return False
        except OTP.DoesNotExist:
            return False
        
    def otp_validated(self, email):
        try:
            otp_record = OTP.objects.get(email=email)
            if otp_record.verified_at:
                return True
            return False
        except OTP.DoesNotExist:
            return False