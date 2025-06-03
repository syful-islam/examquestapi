from oauth2_provider.models import AccessToken, Application
from datetime import datetime, timedelta
from oauthlib.common import generate_token

class AuthService:
    @staticmethod
    def create_access_token(user, application_name):
        application = Application.objects.get(name=application_name)
        expires = datetime.now() + timedelta(days=1)
        access_token = AccessToken.objects.create(
            user=user,
            application=application,
            expires=expires,
            token=generate_token()
        )
        return access_token

    @staticmethod
    def validate_access_token(token):
        try:
            access_token = AccessToken.objects.get(token=token)
            if access_token.is_valid():
                return access_token.user
            else:
                return None
        except AccessToken.DoesNotExist:
            return None
        except Exception as e:
            # Handle any other exceptions that may arise
            print(f"Error validating token: {e}")
            return None

    @staticmethod
    def get_user_by_token(token):
        try:
            access_token = AccessToken.objects.get(token=token)
            return access_token.user
        except AccessToken.DoesNotExist:
            return None