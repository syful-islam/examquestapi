from django.db import models
from app.modules.subscription.models.subscriber import Subscriber

# Common fields for id and timestamps
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True