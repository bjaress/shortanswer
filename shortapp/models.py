from django.db import models
from django.forms import ModelForm

class Question(models.Model):
    text = models.TextField(
            verbose_name="question text",
            max_length="3000")

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text']
