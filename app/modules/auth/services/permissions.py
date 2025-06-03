
from rest_framework import permissions
from app.modules.access_control.models.user_role import UserRole
from app.modules.access_control.models.role_permission import RolePermission

class IsAuthorized(permissions.BasePermission):
    """
    Permission class that checks permissions specified in 'permission_required'.
    - For ModelViewSet: Appends model name to actions (e.g., 'list' -> 'list_yourmodel').
    - For ReportViewSet: Uses report_name and action (e.g., 'view_software_license').
    - Differentiates 'list' and 'retrieve' with separate permissions.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        # Get user's roles
        user_roles = UserRole.objects.filter(user=request.user).select_related('role')
        role_ids = [ur.role.id for ur in user_roles]

        # Map permission actions to fields in RoleScreenPermission
        permission_field_map = {
            'list': 'can_list',    # Separate permission for list
            'view': 'can_view',    # For retrieve
            'create': 'can_create',
            'edit': 'can_edit',
            'delete': 'can_delete',
            'export': 'can_export',
            'print': 'can_print',
        }

        model_name = view.queryset.model.__name__.lower()
        permission_required = getattr(view, 'permission_required', [])

        if not permission_required:
            return False  # Deny access if no permissions specified

        # Construct full permission names (e.g., 'list' -> 'list_yourmodel')
        full_permissions = [f"{perm}_{model_name}" for perm in permission_required]

        # Map DRF actions to permission actions
        action_map = {
            'list': 'list',    # Maps to 'list' permission
            'retrieve': 'view', # Maps to 'view' permission
            'create': 'create',
            'update': 'edit',
            'partial_update': 'edit',
            'destroy': 'delete',
        }
        required_action = action_map.get(view.action)
        if not required_action:
            return True  # Allow custom actions if not mapped

        # Check if the required action is in the permission list
        required_permission = f"{required_action}_{model_name}"
        if required_permission not in full_permissions:
            return False

        permission_field = permission_field_map.get(required_action, 'can_view')
        return RolePermission.objects.filter(
            role__id__in=role_ids,
            screen_permission__name=required_permission,
            **{permission_field: True}
        ).exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)