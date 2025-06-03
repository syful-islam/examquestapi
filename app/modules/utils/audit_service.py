# middleware.py (to track the user making changes)
class AuditServiceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method in ['POST', 'PUT', 'PATCH']:
            request._audit_user = request.user if request.user.is_authenticated else None
        return None