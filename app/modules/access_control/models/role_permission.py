from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel
from app.modules.access_control.models.role import Role
from app.modules.access_control.models.screen import Screen

class RolePermission(AdminBaseModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_list = models.BooleanField(default=False)
    can_export = models.BooleanField(default=False)
    can_print = models.BooleanField(default=False)

    class Meta:
        unique_together = ('role', 'screen_permission')

    def __str__(self):
        return f"{self.role.name} - {self.screen_permission.name}"