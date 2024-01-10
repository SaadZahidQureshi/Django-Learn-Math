from django.db import models
from customAuth.models import BaseModel
from customAuth.CharFieldSizes import CharFieldSizes
# Create your models here.
class Category(BaseModel):
    category_title = models.CharField(max_length=CharFieldSizes.XXX_LARGE)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to='category_images')
