from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home_page(request):
    return render(request, 'shortapp/home.html')

def question_form(request):
    if request.method == 'GET':
        return render(request, 'shortapp/question_form.html')
    if request.method == 'POST':
        #TODO save question and get ID
        #request.POST['question']
        question_id = 1 #TODO
        return HttpResponseRedirect('/question/'+str(question_id))

def question(request, identifier):
    return render(request, 'shortapp/question.html')
