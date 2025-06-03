from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel
tax_type_choices = [
    ('GST', 'GST'),
    ('VAT', 'VAT')
]
class Subscriber(AdminBaseModel):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address_line1 = models.TextField(null=True, blank=True)
    address_line2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    tax_type = models.CharField(max_length=100, null=True, blank=True, choices=tax_type_choices)
    terms_and_conditions = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100,default="Active")
    subscription_id = models.IntegerField(null=True, blank=True) #current subscription id