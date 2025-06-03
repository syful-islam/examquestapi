from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel

class Role(AdminBaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name