from django.db import models
from customAuth.models import BaseModel
from customAuth.CharFieldSizes import CharFieldSizes
from enum import Enum

# Create your models here.

class CATEGORY_LIST(Enum):
    CALCULUS = 'Calculus'
    GEOMETERY = 'Geometery'
    TRIGONOMETERY = 'Trigonometery'
    ALGEBRA = 'Algebra'

    @staticmethod
    def choices():
        return [(item.value, item.value) for item in CATEGORY_LIST]


# CATEGORY_LIST = [('Calculus','Calculus'),('Geometery','Geometery'),('Trigonometery','Trigonometery'),('Algebra','Algebra')]
    
class Category(BaseModel):
    category_title = models.CharField(max_length=CharFieldSizes.XXX_LARGE, choices = CATEGORY_LIST.choices())
    category_description = models.TextField()
    category_image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.category_title
