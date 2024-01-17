# forms.py
from customAuth.forms import StandardForm
from .models import Category, Level, Question
from django import forms

class CategoryForm(StandardForm):

    # category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model= Category
        fields = ['category_title', 'category_description','category_image']


class LevelForm(StandardForm):

    # category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model= Level
        fields = ['level_no', 'number_of_questions','level_category']



class QuestionForm(StandardForm):

    # category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model= Question
        fields = ['question_title', 'question_description','option_a','option_b','option_c','option_d','correct_answer','question_level','question_helping_video','question_image','question_countdown_time']