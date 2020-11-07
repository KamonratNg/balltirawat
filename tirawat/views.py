from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Home(request):
	return render(request,'tirawat/home.html')

def About(request):
	return render(request,'tirawat/about.html')

def Research(request):
	return render(request,'tirawat/research.html')

def Service(request):
	return render(request,'tirawat/service.html')

def Contact(request):
	return render(request,'tirawat/contact.html')


