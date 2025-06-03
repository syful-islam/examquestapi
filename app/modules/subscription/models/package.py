from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel

class Package(AdminBaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=100)
    max_users = models.IntegerField()
    max_storage = models.IntegerField(blank=True, null=True,default=0)
    max_transaction = models.IntegerField(blank=True, null=True,default=0) #Transaction per day. Reset every day.
    priority_support = models.BooleanField(blank=True, null=True, default=False)  