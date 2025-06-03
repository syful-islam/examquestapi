from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from yourapp.models import AccessToken

class TokenAuthWithSubscriber(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return None

        token = token.split(' ')[1]

        try:
            access_token = AccessToken.objects.select_related('user__subscriber').get(token=token)
            request.subscriber = access_token.user.subscriber  # Attach subscriber globally
            return (access_token.user, None)
        except AccessToken.DoesNotExist:
            raise AuthenticationFailed('Invalid or expired token')
