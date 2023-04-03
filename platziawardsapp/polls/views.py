from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello world!')

def detail(request, question_id):
    return HttpResponse(f'You are watching the question Nº {question_id}')

def results(request, question_id):
    return HttpResponse(f'You are watching the result of the question Nº {question_id}')

def vote(request, question_id):
    return HttpResponse(f'You are voting for question Nº {question_id}')