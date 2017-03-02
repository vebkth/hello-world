from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return httpResponse('')

def detail(request):
	return HttpResponse('this is not what youre looking for')


def contact(request):
	return HttpResponse('')

# Create your views here.
