from rest_framework import serializers
from app.modules.general_module.serializers.custom_fields import ANDateTimeField

class AdminBaseModelSerializer(serializers.ModelSerializer):
    created_at = ANDateTimeField(read_only=True)
    updated_at = ANDateTimeField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)