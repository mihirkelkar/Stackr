from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def homepage(request):
  return render_to_response('home.html')

def packr(request):
  return render_to_response('packr.html')

def stackr(request):
  return render_to_response('stackr.html')
