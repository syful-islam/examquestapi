from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel
from app.modules.subscription.models.package import Package
from app.modules.subscription.models.subscriber import Subscriber

class Subscription(AdminBaseModel):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.PROTECT, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.PROTECT, null=True, blank=True)
    features = models.JSONField(default=dict)
    status = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    renewal_date = models.DateTimeField()