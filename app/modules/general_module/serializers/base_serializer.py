from rest_framework import serializers
from app.modules.general_module.serializers.custom_fields import ANDateTimeField
from app.core.logger import log

class BaseModelSerializer(serializers.ModelSerializer):
    created_at = ANDateTimeField(read_only=True)
    updated_at = ANDateTimeField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Mark 'subscriber' as read_only if it exists in the serializer fields
        if 'subscriber' in self.fields:
            self.fields['subscriber'].read_only = True