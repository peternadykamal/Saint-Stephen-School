from threading import local
from django.db import models
from django.contrib.auth.models import Permission
from django.db import transaction, IntegrityError

import uuid


class UserPermissionTag(models.Model):
  tag_name = models.CharField(max_length=100, unique=True)
  permissions = models.ManyToManyField(Permission, blank=True)

  parent = models.ForeignKey(
      "UserPermissionTag", related_name="parent_tag", on_delete=models.SET_NULL, null=True, blank=True)
  child = models.ForeignKey(
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
  def _lock_tag_if_exits(tag_id):
    try:
      tag = UserPermissionTag.objects.select_for_update().get(id=tag_id)
    except:
      tag = None
    return tag

  @staticmethod
  def _lock_highest_tag():
    try:
      tag = UserPermissionTag.objects.select_for_update().get(is_top=True)
    except:
      tag = None
    return tag

  @staticmethod
  def _lock_lowest_tag():
    try:
      tag = UserPermissionTag.objects.select_for_update().get(is_buttom=True)
    except:
      tag = None
    return tag

  def updateHighestTag():
    try:
      tag = UserPermissionTag.objects.select_for_update().get(is_top=True)
      tag.is_top = False
      tag.save()
    except:
      ''''''
    try:
      tag = UserPermissionTag.objects.select_for_update().get(parent=None)
      tag.is_top = True
      tag.save()
    except:
      ''''''

  def updateLowestTag():
    try:
      tag = UserPermissionTag.objects.select_for_update().get(is_buttom=True)
      tag.is_buttom = False
      tag.save()
    except:
      ''''''
    try:
      tag = UserPermissionTag.objects.select_for_update().get(child=None)
      tag.is_buttom = True
      tag.save()
    except:
      ''''''

  @staticmethod
  def swap_tags(tag1: "UserPermissionTag", tag2: "UserPermissionTag"):
    with transaction.atomic():
      if tag1 is None or tag2 is None or tag1 == tag2:
        return

      def updateAndRetriveTags():
        nonlocal tag1, tag2
        if tag1.parent:
          tag1.parent.save()
        if tag1.child:
          tag1.child.save()
        if tag2.parent:
          tag2.parent.save()
        if tag2.child:
          tag2.child.save()
        tag1.save()
        tag2.save()
        tag1 = UserPermissionTag._lock_tag(tag1.id)
        tag2 = UserPermissionTag._lock_tag(tag2.id)

      if tag2.parent == tag1:
        tag1.child, tag2.child, tag2.parent, tag1.parent = tag2.child, tag1, tag1.parent, tag2
        updateAndRetriveTags()
        if tag1.child:
          tag1.child.parent = tag1
          updateAndRetriveTags()
        if tag2.parent:
          tag2.parent.child = tag2
          updateAndRetriveTags()
      elif tag1.parent == tag2:
        tag1.child, tag2.child, tag1.parent, tag2.parent = tag2, tag1.child, tag2.parent, tag1
        updateAndRetriveTags()
        if tag2.child:
          tag2.child.parent = tag2
          updateAndRetriveTags()
        if tag1.parent:
          tag1.parent.child = tag1
          updateAndRetriveTags()
      else:
        tag1.child, tag2.child = tag2.child, tag1.child
        tag1.parent, tag2.parent = tag2.parent, tag1.parent
        updateAndRetriveTags()

        # Update child references for tag1 and tag2
        if tag1.child:
          tag1.child.parent = tag1
          updateAndRetriveTags()

        if tag2.child:
          tag2.child.parent = tag2
          updateAndRetriveTags()

        # Update parent references for tag1's and tag2's parent
        if tag1.parent:
          tag1.parent.child = tag1
          updateAndRetriveTags()

        if tag2.parent:
          tag2.parent.child = tag2
          updateAndRetriveTags()

      UserPermissionTag.updateHighestTag()
      UserPermissionTag.updateLowestTag()

  @staticmethod
  def delete_tag(tag: "UserPermissionTag"):
    with transaction.atomic():
      parent = tag.parent
      child = tag.child

      tag.delete()

      if tag.parent:
        parent.child = child
        parent.save()
      if tag.child:
        child.parent = parent
        child.save()

      UserPermissionTag.updateHighestTag()
      UserPermissionTag.updateLowestTag()

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
        if highestTag:
          highestTag.parent = tag
          highestTag.save()
        tag.child = highestTag

      tag.parent = parent
      tag.save()

      UserPermissionTag.updateHighestTag()
      UserPermissionTag.updateLowestTag()

  @staticmethod
  def move_up(tag: "UserPermissionTag"):
    with transaction.atomic():
      parent = UserPermissionTag._lock_tag_if_exits(tag.parent.id)
      if parent:
        UserPermissionTag.swap_tags(tag, parent)

  @staticmethod
  def move_down(tag: "UserPermissionTag"):
    with transaction.atomic():
      child = UserPermissionTag._lock_tag_if_exits(tag.child.id)
      if child:
        UserPermissionTag.swap_tags(tag, child)

  # TODO test case this method
  def has_permission(self, required_permission):
    # make sure this permission is in the database
    if not Permission.objects.filter(codename=required_permission).exists():
      return False
    return required_permission in [item.codename for item in self.permissions.all()]
