from django.db import models
from django.forms import ModelForm

class Question(models.Model):
    text = models.TextField()

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text']
