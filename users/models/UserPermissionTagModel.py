import re
import uuid
from threading import local

from cv2 import add
from django.contrib.auth.models import Permission, User
from django.db import IntegrityError, models, transaction
from django.test import tag


class UserPermissionTag(models.Model):
  order = models.IntegerField(default=-1)
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

  @staticmethod
  def _perform_swap(tag1: "UserPermissionTag", tag2: "UserPermissionTag"):
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
    UserPermissionTag._updateTagsOrder()

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

  def _updateTagsOrder():
    try:
      tag = UserPermissionTag.objects.select_for_update().get(is_top=True)
      order = 0
      while tag:
        tag.order = order
        tag.save()
        order += 1
        tag = tag.child
    except:
      ''''''

  @staticmethod
  def swap_tags(tag1: "UserPermissionTag", tag2: "UserPermissionTag"):
    with transaction.atomic():
      UserPermissionTag._perform_swap(tag1, tag2)

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
      UserPermissionTag._updateTagsOrder()

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
      UserPermissionTag._updateTagsOrder()

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

  @staticmethod
  def get_sorted_tags() -> list['UserPermissionTag']:
    """Returns a list of tags sorted from top to buttom"""
    tag = UserPermissionTag.objects.get(is_top=True)
    tags = []

    while tag:
      tags.append(tag)
      tag = tag.child
    return tags

  @staticmethod
  @transaction.atomic
  def update_hierarchy(newHierarchy: list['UserPermissionTag']):
    # make sure all tags in new hierarchy are unique
    if len(newHierarchy) != len(set(newHierarchy)):
      raise Exception("All tags in the new hierarchy must be unique.")

    # newHierarchyTags = [tag.tag_name for tag in newHierarchy]

    # make sure the first and last tags in the hierarchy are not changed
    oldHierarchy = UserPermissionTag.get_sorted_tags()
    condition = oldHierarchy[0].id != newHierarchy[0].id or oldHierarchy[-1].id != newHierarchy[-1].id

    if (condition):
      raise Exception(
          "first and last tags in the hierarchy can't be changed.")

    for i in range(len(newHierarchy)):
      oldHierarchy = UserPermissionTag.get_sorted_tags()
      if (len(oldHierarchy) != len(newHierarchy)):
        raise Exception(
            "The new hierarchy is not the same length as the old one.")
      else:
        if oldHierarchy[i].id != newHierarchy[i].id:
          # get new hierarchy tag from oldHierarchy list,
          # we do so to get new tag with updated child and parent pointers
          newTag = next(tag for tag in oldHierarchy if tag.id ==
                        newHierarchy[i].id)
          UserPermissionTag._perform_swap(oldHierarchy[i], newTag)

  def add_permission(self, permission_codename):
    """ take a permission codename and add it to this tag"""

    # first check if the permission exists
    try:
      permission = Permission.objects.get(codename=permission_codename)
    except Permission.DoesNotExist:
      raise Exception("Permission does not exist.")

    # check if the permission is already added
    if self.permissions.filter(codename=permission_codename).exists():
      return

    # add the permission
    self.permissions.add(permission)

  def has_permission(self, required_permission):
    """ take a permission codename and return true if this tag has that permission"""
    return self.permissions.filter(codename=required_permission).exists()

  @staticmethod
  def get_highest_tag(tags: list['UserPermissionTag'], return_order=False):
    ''' take a list of tags and return the highest permission tag'''
    # check first if tags in database
    if UserPermissionTag.objects.count() == 0:
      if return_order:
        return None, -1
      else:
        return None

    if len(tags) == 0:
      if return_order:
        return None, -1
      else:
        return None
    elif len(tags) == 1:
      if return_order:
        return tags[0], tags[0].order
      else:
        return tags[0]
    else:
      # sort tags by order, and return new list
      sortedTags = sorted(tags, key=lambda tag: tag.order)
      if return_order:
        return sortedTags[0], sortedTags[0].order
      else:
        return sortedTags[0]
