from django.db import models

class OTP(models.Model):
    email = models.CharField(max_length=100)
    otp = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_time = models.DateTimeField()
    verified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('email', 'otp')