from django.contrib import admin

from .models import Category, QuestionAnswer

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('text', 'completed')

@admin.register(QuestionAnswer)
class QuestionAnswerCategory(admin.ModelAdmin):
    list_display = ('text', 'completed')
