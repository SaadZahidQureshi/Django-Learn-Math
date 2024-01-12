from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from customAuth.models import BaseModel
from customAuth.CharFieldSizes import CharFieldSizes
from enum import Enum
from PIL import Image


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



@receiver(post_save, sender=Category)
def resize_image(sender,instance, **kwargs):

    if hasattr(instance, 'category_image'):
        img = Image.open(instance.category_image.path)
        resized_img = img.resize((400, 209))
        resized_img.save(instance.category_image.path)


class Level(BaseModel):
    level_no = models.IntegerField(unique=True)
    number_of_questions = models.IntegerField()
    level_category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"Level {self.level_no}"