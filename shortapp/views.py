from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import QuestionForm, Question

# Create your views here.
def home_page(request):
    return render(request, 'shortapp/home.html')

def question_form(request):
    if request.method == 'GET':
        return render(request, 'shortapp/question_form.html',
                {'form': QuestionForm()})
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save()
            return HttpResponseRedirect('/question/'+str(new_question.id))
        else:
            print(form.errors)

def question(request, identifier):
    return render(request, 'shortapp/question.html',
            {'question': Question.objects.get(id=int(identifier))})
