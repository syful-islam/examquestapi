from django.db import models
from app.modules.general_module.models.base_model import BaseModel

class Document(BaseModel):
    parent_type = models.CharField(max_length=100) #eg software, supplier, contract
    parent_id = models.IntegerField() #id of the parent
    document_name = models.CharField(max_length=255,blank=True, null=True)

    def upload_to(instance, filename):
        return f'{instance.parent_type}/{instance.parent_id}/{filename}'

    document_file = models.FileField(upload_to=upload_to)