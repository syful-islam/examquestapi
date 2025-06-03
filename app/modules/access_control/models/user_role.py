from django.db import models
from app.modules.general_module.models.admin_base_model import AdminBaseModel
from app.modules.access_control.models.role import Role
from app.modules.student_management.models import EQUser

class UserRole(AdminBaseModel):
    user = models.ForeignKey(EQUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.email} - {self.role.name}"