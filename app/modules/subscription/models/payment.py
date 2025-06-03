from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel

class SubscriptionPayment(AdminBaseModel):
    subscription_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=100)
    payment_id = models.IntegerField()
    status = models.CharField(max_length=100)
    