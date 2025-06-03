from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel

class Screen(AdminBaseModel):
    name = models.CharField(max_length=100, unique=True)  # e.g., "user", "employee"
    description = models.TextField(blank=True)
    module = models.CharField(max_length=100)  # e.g., "SAM", "RFP"
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name