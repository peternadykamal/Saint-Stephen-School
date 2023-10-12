import http
import json
from ast import mod

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (require_GET, require_http_methods,
                                          require_POST)
from numpy import require

from decorators.checkPermissionDecorator import has_permission_tag
from users import models
from users.forms import UserPermissionTagForm


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
@ require_GET
def getTag(request):
  # get the tag id from the request
  tag_id = request.GET.get('id', None)
  if tag_id:
    tag = get_object_or_404(models.UserPermissionTag, id=tag_id)
    form = UserPermissionTagForm(
        instance=tag)
    form_html = render(request, 'tags/tagForm.html',
                       {'form': form, "tag": tag})
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
@ require_POST
def updateHierarchy(request):
  try:
    requestData = json.loads(request.body.decode('utf-8'))
    newHierarchy = requestData['newHierarchy']
    newTags = [get_object_or_404(
        models.UserPermissionTag, id=tag) for tag in newHierarchy]
    models.UserPermissionTag.update_hierarchy(newTags)
    response_data = {'status': 'success'}
    return JsonResponse(response_data)
  except Exception as e:
    print(e)
    response_data = {'status': 'fail'}
    return JsonResponse(response_data)


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
@ require_POST
def updateTag(request):
  tag_id = request.POST.get('id', None)
  if tag_id:
    tag = get_object_or_404(models.UserPermissionTag, id=tag_id)
    form = UserPermissionTagForm(data=request.POST, instance=tag)
    if (form.is_valid()):
      form.save()
      return JsonResponse({'status': 'success'})
    else:
      form_html = render(request, 'tags/tagForm.html', {'form': form})
      form_html = str(form_html.content, encoding='utf8')
      return JsonResponse({'status': 'fail', "form_html": form_html})


@ login_required(login_url='sign-in')
@ has_permission_tag(tag_name='admin')
@ require_POST
def addTag(request):
  form = UserPermissionTagForm(data=request.POST)
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
@ require_http_methods(["DELETE"])
def deleteTag(request, tag_id):
  tag = get_object_or_404(models.UserPermissionTag, id=tag_id)
  if not tag.is_buttom and not tag.is_top:
    models.UserPermissionTag.delete_tag(tag)
    return JsonResponse({'status': 'success'})
  else:
    return JsonResponse({'status': 'fail'})
