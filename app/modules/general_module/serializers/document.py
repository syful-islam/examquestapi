from rest_framework import serializers
from ..models.document import Document
from app.modules.general_module.serializers.base_serializer import BaseModelSerializer

class DocumentSerializer(BaseModelSerializer,serializers.ModelSerializer):
    # parent_type = serializers.CharField(read_only=True)
    # parent_id = serializers.IntegerField(read_only=True)
    document_file_name = serializers.SerializerMethodField()
    # document_file_link = serializers.SerializerMethodField()
    
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    def get_document_file_name(self, obj):
        """Retrieve the file name of the document."""
        return obj.document_file.name.split('/')[-1] if obj.document_file else None
    
    # def get_document_file_link(self, obj):
    #     """Retrieve the file link of the document."""
    #     return obj.document_file.url if obj.document_file else None
    
    # def get_document_file_link(self, obj):
    #     """Retrieve the file link of the document."""
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.document_file.url)
        # return obj.document_file.url if obj.document_file else None
    
    # def get_document_file_link(self, obj):
    #     request = self.context.get('request')
    #     if request and hasattr(obj.document_file, 'url'):
    #         return request.build_absolute_uri(obj.document_file.url)
    #     elif hasattr(obj.document_file, 'url'):
    #         # fallback to relative URL if request is None
    #         return obj.document_file.url
    #     return None