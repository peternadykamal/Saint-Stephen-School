import json
import re
from multiprocessing import context
from urllib import request

from click import echo
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
from django.views.decorators.http import (require_GET, require_http_methods,
                                          require_POST)
from waitress import profile

from users.forms import ProfileForm


def renderTestTemplate(request):
  context = {'form': ProfileForm()}
  return render(request, 'testTemplate.html', context)


@require_POST
def testPost(request):
  # check request attributes
  print(f'request.body: {request.body}')
  # convert to json
  requestData = QueryDict(request.body)
  # convert to dict
  requestData = {key: value for key, value in requestData.items()}
  print(requestData)

  echo = request.POST.get('echo')

  return JsonResponse({'message': 'Hello, World!', 'echo': f'{echo} from server'})


@require_GET
def testGet(request):
  # get request attributes
  echo = request.GET.get('echo')
  params = request.GET.get('param')
  return JsonResponse({'message': 'Hello, World!', 'echo': f'{echo} from server'})


def testSearch(request):
  if request.method == 'GET':
    search = request.GET.get('search')
    age = request.GET.get('age')
    print(request.GET.get('search'))
    print(request.GET.get('age'))
    return JsonResponse({'search': f'{search}', 'age': f'{age}', 'method': 'GET'})
  elif request.method == 'POST':
    return JsonResponse({'method': 'POST'})

# this path gets the user profile data


def profileTest(request):
  profileForm = ProfileForm()
  if request.method == 'POST':
    profileForm = ProfileForm(request.POST)
    if profileForm.is_valid():
      profileForm.save()
      return JsonResponse({'status': 'success'})
    else:
      return JsonResponse({'status': 'fail'})
  elif request.method == 'GET':
    profileForm = ProfileForm()
    return render(request, 'testTemplate.html', {'form': profileForm})
