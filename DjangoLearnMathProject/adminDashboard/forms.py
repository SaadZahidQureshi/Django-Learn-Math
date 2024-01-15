# forms.py
from customAuth.forms import StandardForm
from .models import Category, Level
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