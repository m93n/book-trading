from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class MyAccountManager(BaseUserManager):
    def create_user(self, email, mobile_number, username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        if not mobile_number:
            raise ValueError("User must have a mobile number")
        

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            mobile_number = mobile_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, mobile_number,username, password):
        user = self.create_user(
            email    = self.normalize_email(email),
            username = username,
            password = password,
            mobile_number = mobile_number
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    full_name       = models.CharField(max_length=40, verbose_name='full name')
    mobile_number   = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex=r'09(\d{9})$')])
    mobile_number_verified = models.BooleanField(default=False)
    date_of_birth   = models.DateField(verbose_name='date of birth', null=True)
    home_address    = models.TextField()
    postal_code     = models.CharField(max_length=15)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','mobile_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def craete_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)