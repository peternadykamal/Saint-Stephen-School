from django.db import models
from django.contrib.auth.models import Permission
from django.db import transaction, IntegrityError

import uuid


class UserPermissionTag(models.Model):
  tag_name = models.CharField(max_length=100, unique=True)
  permissions = models.ManyToManyField(Permission, blank=True)

  parent = models.OneToOneField(
      "UserPermissionTag", related_name="parent_tag", on_delete=models.SET_NULL, null=True, blank=True)
  child = models.OneToOneField(
      "UserPermissionTag", related_name="child_tag", on_delete=models.SET_NULL, null=True, blank=True)
  is_top = models.BooleanField(default=False)
  is_buttom = models.BooleanField(default=False)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.tag_name

  @staticmethod
  def _lock_tag(tag_id):
    try:
      tag = UserPermissionTag.objects.select_for_update().get(id=tag_id)
    except:
      raise Exception("Tag id not found.")
    return tag

  @staticmethod
  def _lock_highest_tag():
    try:
      tag = UserPermissionTag.objects.select_for_update().get(parent=None)
    except:
      tag = None
    return tag

  @staticmethod
  def swap_tags(tag1_id, tag2_id):
    with transaction.atomic():
      tag1 = UserPermissionTag._lock_tag(tag1_id)
      tag2 = UserPermissionTag._lock_tag(tag2_id)

      tag1.child, tag2.child = tag2.child, tag1.child
      tag1.parent, tag2.parent = tag2.parent, tag1.parent

      tag1.save()
      tag2.save()

  @staticmethod
  def delete_tag(tag_id):
    with transaction.atomic():
      tag = UserPermissionTag._lock_tag(tag_id)
      if tag.parent:
        parent = tag.parent
        parent.child = tag.child
        parent.save()
      if tag.child:
        child = tag.child
        child.parent = tag.parent
        child.save()

      tag.delete()

  @staticmethod
  def insert_tag(tag: "UserPermissionTag", parent_id=None):
    with transaction.atomic():
      if parent_id is not None:
        parent = UserPermissionTag._lock_tag(parent_id)
        if parent.child:
          child_of_parent = parent.child
          tag.child = child_of_parent
          child_of_parent.parent = tag
          child_of_parent.save()
        else:
          tag.child = None
        parent.child = tag
        parent.save()
      else:
        parent = None
        highestTag = UserPermissionTag._lock_highest_tag()
        highestTag.parent = tag
        tag.child = highestTag
        highestTag.save()

      tag.parent = parent
      tag.save()

  @staticmethod
  def move_up(tag_id):
    with transaction.atomic():
      tag = UserPermissionTag._lock_tag(tag_id)
      sibling = tag.parent.child_tag.filter(
          idlt=tag_id).order_by('-id').first()
      if sibling:
        UserPermissionTag.swap_tags(tag_id, sibling.id)

  @staticmethod
  def move_down(tag_id):
    with transaction.atomic():
      tag = UserPermissionTag._lock_tag(tag_id)
      sibling = tag.parent.child_tag.filter(
          idgt=tag_id).order_by('id').first()
      if sibling:
        UserPermissionTag.swap_tags(tag_id, sibling.id)
