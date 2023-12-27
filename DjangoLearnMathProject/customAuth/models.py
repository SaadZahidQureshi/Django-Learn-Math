from django.db import models
from datetime import datetime
# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserVerification(TimeStampMixin, models.Model):
    userverification_id=models.AutoField(primary_key=True, null=False)
    email=models.EmailField(unique=True, blank=False, null=False)
    otp= models.IntegerField()
    is_verified= models.BooleanField()

    def __str__(self):
        return str(self.email)
    
class Users(TimeStampMixin,models.Model):
    user_id = models.AutoField(primary_key=True, null=False, blank=False)
    user_email = models.EmailField(unique=True, blank=False, null=False)
    user_name = models.CharField(max_length=100, blank=False)
    user_password = models.CharField(max_length=100, blank=False)
    user_image_url = models.URLField(null=True)
    is_active = models.BooleanField(null=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.ForeignKey(UserVerification, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.user_id)

    @property
    def is_verified(self):
        verifciation_instance = UserVerification.objects.filter(email=self.user_email).first()

        if verifciation_instance:
            return verifciation_instance.is_verified
        return False
