from rest_framework import serializers

class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class OTPValidateSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=10)