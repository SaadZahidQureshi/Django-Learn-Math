from django.contrib.auth.models import AbstractUser, BaseUserManager
from customAuth.CharFieldSizes import CharFieldSizes
from django.db import models
from enum import Enum


class OTPtypes(Enum):
    CREATE_USER = 'create'
    FORGOT_PASSWORD = 'forgot'
    UPDATE_EMAIL = 'update_email'
    UPDATE_PHONE = 'update_phone'

    @staticmethod
    def get_enum_set():
        return set(item.value for item in OTPtypes)

    @staticmethod
    def choices():
        return [(item.value, item.value) for item in OTPtypes]
    
    @classmethod
    def profile_choices(cls):
        return [(cls.UPDATE_PHONE.value, cls.UPDATE_PHONE.value), (cls.UPDATE_EMAIL.value, cls.UPDATE_EMAIL.value)]
            # print(datetime.datetime.now().time() , stored_timeout.time())
            # print(datetime.datetime.now().time() < stored_timeout.time())


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class OTP(BaseModel):
    code = models.CharField(max_length=CharFieldSizes.SMALL)
    content = models.CharField(max_length=CharFieldSizes.XX_LARGE)
    verification_token = models.CharField(max_length=CharFieldSizes.XXX_LARGE)
    timeout = models.DateTimeField()
    type = models.CharField(max_length=CharFieldSizes.SMALL, choices=OTPtypes.choices())
    used = models.BooleanField(default=False)
  
    def get_key(self):
        return '_'.join([str(self.type), self.content])

    def __str__(self) -> str:
        return self.content
    

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    username = None
    name = models.CharField(max_length = CharFieldSizes.XX_LARGE)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to="profile_images", default='profile1-blue.svg')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

