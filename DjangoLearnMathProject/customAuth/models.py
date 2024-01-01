from django.contrib.auth.models import AbstractUser, BaseUserManager
from customAuth.CharFieldSizes import CharFieldSizes
from django.db import models
from enum import Enum
# from customAuth import helpers
from customAuth.CharFieldSizes import CharFieldSizes
# from api.jwtauth import helpers
# from api.core.models import CharFieldSizes, CustomResponse, GlobalResponseMessages, BaseModel


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

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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