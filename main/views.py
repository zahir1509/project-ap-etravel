from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

def homepage(request):
    return render(request, 'base.html')