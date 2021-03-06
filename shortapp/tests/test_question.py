#from django.core.urlresolvers import resolve
from django.test import TestCase, Client
from django.http import HttpRequest
from django.contrib.auth import get_user_model
User = get_user_model()

from hamcrest import assert_that
from hamcrest import contains_string, equal_to, ends_with

from ..views import question
from ..models import Question

QUESTION_TEXT = "What brought you here, friend Geppetto?"

class QuestionTest(TestCase):

    def test_ask_question(self):
        User.objects.create_user('test', password='test')
        client = Client()
        client.login(username='test', password='test')
        response = client.post('/question', {'text': QUESTION_TEXT})

        new_question = Question.objects.latest('id')
        assert_that(new_question.text, equal_to(QUESTION_TEXT),
                "Asked questions should be saved.")
        assert_that(response['Location'],
                ends_with('question/'+str(new_question.id)),
                "The question should be shown after it is saved.")

    def test_show_question(self):
        new_question = Question(text=QUESTION_TEXT)
        new_question.save()

        request = HttpRequest()
        request.method = 'GET'
        response = question(request, str(new_question.id))

        assert_that(response.content.decode(),
                contains_string(QUESTION_TEXT),
                "An existing answer should have its own page.")

