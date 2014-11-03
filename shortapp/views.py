from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import QuestionForm, Question
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

# Create your views here.
def home_page(request):
    return render(request, 'shortapp/home.html')

@login_required
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

def login_debug(request):
    """Special debug-only login.

    Trying to set up test users in a functional test is a massive
    nightmare, so we just let users log in by just hitting a URL, but
    only in DEBUG mode.

    If you think this is clumsy, you should see the recommended
    solutions that didn't work.

    """

    if settings.DEBUG:
        user = User.objects.get(username='debug')
        if user == None:
            user = User.objects.create_user('debug', password='debug')
        user = authenticate(username='debug', password='debug')
        auth_login(request, user)
    return HttpResponse(settings.DEBUG, content_type="text/plain")

def logout(request):
    """Let anyone logout by hitting this URL."""
    auth_logout(request)
    return HttpResponseRedirect('/')
