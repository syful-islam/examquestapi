from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel

class AuditLog(AdminBaseModel):
    resource_name = models.CharField(max_length=100, null=True, blank=True)
    object_id = models.CharField(max_length=100, null=True, blank=True)
    action = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default='success')
    changes = models.JSONField(null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    subscriber_id =  models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    ip_address = models.CharField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.resource_name} [{self.action}] by {self.user} at {self.timestamp}"