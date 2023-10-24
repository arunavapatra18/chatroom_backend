from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext as _


# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Method to create a new user and save it to the database

        Args:
            email (char): Email of the user
            password (char): Password of the user

        Raises:
            ValueError: If email is not set, raise error

        Returns:
            model: user model
        """
        if not email:
            raise ValueError('The given email must be set!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, passsword, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            passsword (_type_): _description_

        Returns:
            _type_: _description_
        """
        extra_fields.setdefault('is_stuff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, passsword, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        """_summary_

        Args:
            email (_type_): _description_
            password (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        extra_fields.setdefault('is_stuff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have isStaff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=30, null=False, blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
