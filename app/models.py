from django.db import models
from app.modules.general_module.models.base_model import BaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password
from app.modules.subscription.models.subscriber import Subscriber

# Custom user manager
class UserManager(BaseUserManager):    
    def create_user(self, full_name, email, mobile_no, password=None,subscriber=None, is_admin=False,created_by=None, updated_by=None):
        if not full_name:
            raise ValueError("Users must have a full_name")
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)

        user = self.model(
            # username=username,
            full_name=full_name,
            email=email,
            mobile_no=mobile_no,
            subscriber=subscriber,
            is_admin=is_admin,
            created_by=created_by,
            updated_by=updated_by
        )
        user.set_password(password)  # This will hash the password
        user.save(using=self._db)  # Save the user to the database
        return user

    def create_superuser(self, full_name, email, mobile_no, password=None):
        user = self.create_user(
            # username=username,
            full_name=full_name,
            email=email,
            mobile_no=mobile_no,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def check_password(self, user, password):
        return check_password(password, user.password)
    
class EQUser(AbstractBaseUser,  BaseModel): #PermissionsMixin,
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Stored as a hashed password
    email_verified_at = models.DateTimeField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.PROTECT, null=True, blank=True)
    is_admin = models.BooleanField(default=False)  # Required for admin access
    is_superuser = models.BooleanField(default=False)  # Required for superuser access

    objects = UserManager()  # Link custom manager

    USERNAME_FIELD = "email"  # Use email instead of username for authentication
    REQUIRED_FIELDS = ["full_name","mobile_no"]  # Required fields for superuser creation

    def __str__(self):
        return self.full_name