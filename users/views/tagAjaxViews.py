import http
import json
from ast import mod

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import get_object_or_404, redirect, render

from decorators.checkPermissionDecorator import has_permission_tag
from users import models
from users.forms import UserPermissionTagForm


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
def getTag(request):
  if request.method == 'GET':
    # get the tag id from the request
    tag_id = request.GET.get('id', None)
    if tag_id:
      tag = get_object_or_404(models.UserPermissionTag, id=tag_id)
      form = UserPermissionTagForm(
          instance=tag)
      form_html = render(request, 'tags/tagForm.html', {'form': form})
      form_html = str(form_html.content, encoding='utf8')
      return JsonResponse({"form_html": form_html})
    else:
      # to render the form for adding new tag
      form = UserPermissionTagForm()
      form_html = render(request, 'tags/tagForm.html',
                         {'form': form, "new_tag": True})
      form_html = str(form_html.content, encoding='utf8')
      return JsonResponse({"form_html": form_html})


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
def updateHierarchy(request):
  try:
    if request.method == 'POST':
      requestData = json.loads(request.body.decode('utf-8'))
      newHierarchy = requestData['newHierarchy']
      print(newHierarchy)
      newTags = [models.UserPermissionTag.objects.get(
          id=tag) for tag in newHierarchy]
      models.UserPermissionTag.update_hierarchy(newTags)
      response_data = {'status': 'success'}
      return JsonResponse(response_data)
    else:
      raise Exception("Request method is not POST.")
  except Exception as e:
    print(e)
    response_data = {'status': 'fail'}
    return JsonResponse(response_data)


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
def updateTag(request):
  if request.method == 'POST':
    tag_id = request.POST.get('id', None)
    if tag_id:
      tag = get_object_or_404(models.UserPermissionTag, id=tag_id)
      form = UserPermissionTagForm(
          request.POST, instance=tag)
      print(form.is_valid())
      if (form.is_valid()):
        form.save()
        return JsonResponse({'status': 'success'})
      else:
        form_html = render(request, 'tags/tagForm.html', {'form': form})
        form_html = str(form_html.content, encoding='utf8')
        return JsonResponse({'status': 'fail', "form_html": form_html})

  else:
    return HttpResponse('fail')


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
def addTag(request):
  if request.method == 'POST':
    form = UserPermissionTagForm(request.POST)
    if (form.is_valid()):
      newTag = form.save()
      lastTag = models.UserPermissionTag.objects.get(is_buttom=True)
      models.UserPermissionTag.insert_tag(newTag, lastTag.parent.id)
      return JsonResponse({'status': 'success'})
    else:
      form_html = render(request, 'tags/tagForm.html',
                         {'form': form, "new_tag": True})
      form_html = str(form_html.content, encoding='utf8')
      return JsonResponse({'status': 'fail', "form_html": form_html})


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
def deleteTag(request, tag_id):
  if request.method == 'DELETE':
    tag = get_object_or_404(models.UserPermissionTag, id=tag_id)
    models.UserPermissionTag.delete_tag(tag)
    return JsonResponse({'status': 'success'})
  else:
    return JsonResponse({'status': 'fail'})
