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

def login(request):
  context_object = {}
  context_object.update(csrf(request))
  return render_to_response('login.html', context_object)

def auth_view(request):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username = username, password = password)
  if user is not None:
    auth.login(request, user)
    return HttpResponseRedirect('/loggedin')
  else:
    return HttpResponseRedirect('/invalid')

def loggedin(request):
  return render_to_response('loggedin.html')

def logout(request):
  auth.logout(request)
  return render_to_response('home.html')
