from django.db import models
from app.modules.general_module.models.base_model import BaseModel
from app.modules.student_management.models import SAMUser
# from .software import Software

class Notification(BaseModel):
    user = models.ForeignKey(SAMUser, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)  # eg contract, software, supplier
    supplier = models.CharField(max_length=100, null=True, blank=True)  # name of the supplier
    expiry_date = models.DateTimeField(null=True, blank=True)  # date when the notification expires
    target_type = models.CharField(max_length=100,null=True, blank=True)  # eg software, supplier, contract
    target_id = models.IntegerField(null=True, blank=True)  # id of the target
    target_url = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} for {self.user}"