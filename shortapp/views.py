from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'shortapp/home.html')

def question(request):
    return render(request, 'shortapp/question_form.html')
