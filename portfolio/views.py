from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio

def index(request):
	portfolio_list=Portfolio.objects.all()
	return httpResponse('')

def detail(request):
	return HttpResponse('this is not what youre looking for')


def contact(request):
	return HttpResponse('')

# Create your views here.
