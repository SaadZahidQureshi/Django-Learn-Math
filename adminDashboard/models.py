from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from customAuth.models import BaseModel,User
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


class Category(BaseModel):
    category_title = models.CharField(max_length=CharFieldSizes.XXX_LARGE)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return str(self.id)
    
    def total_questions(self):
        return Question.objects.filter(question_level__level_category = self).count()

@receiver(post_save, sender=Category)
def resize_image(sender,instance, **kwargs):

    if hasattr(instance, 'category_image'):
        img = Image.open(instance.category_image.path)
        resized_img = img.resize((400, 209))
        resized_img.save(instance.category_image.path)


class Level(BaseModel):
    level_no = models.IntegerField()
    number_of_questions = models.IntegerField(default=0)
    level_category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='levels')
    
    class Meta:
        unique_together = ('level_no', 'level_category')

    def __str__(self):
        return str(self.id)
        # return f"Level {self.level_no}"
    
    def total_questions(self):
        return Question.objects.filter(question_level = self).count()
    

class Question(BaseModel):
    question_description = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    question_level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='questions')
    question_helping_video = models.TextField()
    question_image = models.ImageField(upload_to='questions_images', blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Answer(BaseModel):
    selected_option = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    number_of_attempts = models.PositiveIntegerField()
    time_taken = models.CharField(max_length = 255)

    class Meta:
        ordering = ('-updated_at',)
