from django.contrib import admin
from .models import Category,Level,Question
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Level)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'category_description', 'category_image')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_no', 'number_of_questions', 'level_category')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_title', 'question_description', 'question_level', 'question_countdown_time')
    readonly_fields = ('created_at', 'updated_at')