import os

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, tag

# Replace "your_app" with the actual name of your app
from users.models import Profile, UserPermissionTag


class UserPermissionTagTestCase(TestCase):
  basePath = os.path.dirname(__file__) + '/fixtures'
  # List the fixture file paths here
  fixtures = [f'{basePath}/ProfileData.json',
              f'{basePath}/UserData.json',
              f'{basePath}/AddressData.json',
              f'{basePath}/TalmzaLevelData.json',
              f'{basePath}/SchoolLevelData.json',
              ]

  def test_inserting_new_tag(self):
    tag = UserPermissionTag.objects.create(tag_name="t1")

    UserPermissionTag.insert_tag(tag)

    tag = UserPermissionTag.objects.get(tag_name="t1")

    self.assertIsNone(tag.parent)
    self.assertIsNone(tag.child)

    self.assertTrue(tag.is_top)
    self.assertTrue(tag.is_buttom)

  def test_inserting_new_tag(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    # ----------------------------------- tag1 ----------------------------------- #
    self.assertEqual(tag1.parent.id, tag4.id)
    self.assertEqual(tag1.child.id, tag2.id)
    self.assertFalse(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
    # ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag1.id)
    self.assertIsNone(tag2.child)
    self.assertFalse(tag2.is_top)
    self.assertTrue(tag2.is_buttom)
    # ----------------------------------- tag3 ----------------------------------- #
    self.assertIsNone(tag3.parent)
    self.assertEqual(tag3.child.id, tag4.id)
    self.assertTrue(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
    # ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag3.id)
    self.assertEqual(tag4.child.id, tag1.id)
    self.assertFalse(tag4.is_top)
    self.assertFalse(tag4.is_buttom)

  def test_deleting_tags(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    # ------------------------------- deleting Tag3 ------------------------------ #
    # tag4
    # tag1
    # tag2
    tag3 = UserPermissionTag.objects.get(tag_name="t3")

    UserPermissionTag.delete_tag(tag3)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    self.assertIsNone(tag4.parent)
    self.assertEqual(tag4.child.id, tag1.id)
    self.assertTrue(tag4.is_top)
    self.assertFalse(tag4.is_buttom)
    # ------------------------------- deleting Tag1 ------------------------------ #
    # tag4
    # tag2

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    UserPermissionTag.delete_tag(tag1)

    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    self.assertEqual(tag4.child.id, tag2.id)
    self.assertEqual(tag2.parent.id, tag4.id)
    self.assertTrue(tag4.is_top)
    self.assertTrue(tag2.is_buttom)
    # ------------------------------- deleting Tag2 ------------------------------ #
    # tag4

    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    UserPermissionTag.delete_tag(tag2)

    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    self.assertIsNone(tag4.parent)
    self.assertIsNone(tag4.child)

    self.assertTrue(tag4.is_top)
    self.assertTrue(tag4.is_buttom)
    # ------------------------------- deleting Tag4 ------------------------------ #
    #

    tag4 = UserPermissionTag.objects.get(tag_name="t4")
    UserPermissionTag.delete_tag(tag4)

    tags = UserPermissionTag.objects.filter()

    self.assertEqual(len(tags), 0)

  def test_swapping_tags(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    # ------------------------------- swap Tag4 with tag1 ------------------------------ #
    # tag3
    # tag1
    # tag4
    # tag2

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    UserPermissionTag.swap_tags(tag1, tag4)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertEqual(tag1.parent.id, tag3.id)
    self.assertEqual(tag1.child.id, tag4.id)
    self.assertFalse(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag4.id)
    self.assertIsNone(tag2.child)
    self.assertFalse(tag2.is_top)
    self.assertTrue(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertIsNone(tag3.parent)
    self.assertEqual(tag3.child.id, tag1.id)
    self.assertTrue(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag1.id)
    self.assertEqual(tag4.child.id, tag2.id)
    self.assertFalse(tag4.is_top)
    self.assertFalse(tag4.is_buttom)

# ------------------------------- swap Tag1 with tag3 ------------------------------ #
    # tag1
    # tag3
    # tag4
    # tag2

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")

    UserPermissionTag.swap_tags(tag1, tag3)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag3.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag4.id)
    self.assertIsNone(tag2.child)
    self.assertFalse(tag2.is_top)
    self.assertTrue(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag1.id)
    self.assertEqual(tag3.child.id, tag4.id)
    self.assertFalse(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag3.id)
    self.assertEqual(tag4.child.id, tag2.id)
    self.assertFalse(tag4.is_top)
    self.assertFalse(tag4.is_buttom)
# ------------------------------- swap Tag2 with tag3 ------------------------------ #
    # tag1
    # tag2
    # tag4
    # tag3

    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")

    UserPermissionTag.swap_tags(tag2, tag3)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag2.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag1.id)
    self.assertEqual(tag2.child.id, tag4.id)
    self.assertFalse(tag2.is_top)
    self.assertFalse(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag4.id)
    self.assertIsNone(tag3.child)
    self.assertFalse(tag3.is_top)
    self.assertTrue(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag2.id)
    self.assertEqual(tag4.child.id, tag3.id)
    self.assertFalse(tag4.is_top)
    self.assertFalse(tag4.is_buttom)
# ------------------------------- swap Tag3 with tag4 ------------------------------ #
    # tag1
    # tag2
    # tag3
    # tag4

    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    UserPermissionTag.swap_tags(tag3, tag4)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag2.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag1.id)
    self.assertEqual(tag2.child.id, tag3.id)
    self.assertFalse(tag2.is_top)
    self.assertFalse(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag2.id)
    self.assertEqual(tag3.child.id, tag4.id)
    self.assertFalse(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag3.id)
    self.assertIsNone(tag4.child)
    self.assertFalse(tag4.is_top)
    self.assertTrue(tag4.is_buttom)

  def test_move_up_tags(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    # ------------------------------- move tag1 up ------------------------------ #
    # tag3
    # tag1
    # tag4
    # tag2

    tag1 = UserPermissionTag.objects.get(tag_name="t1")

    UserPermissionTag.move_up(tag1)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertEqual(tag1.parent.id, tag3.id)
    self.assertEqual(tag1.child.id, tag4.id)
    self.assertFalse(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag4.id)
    self.assertIsNone(tag2.child)
    self.assertFalse(tag2.is_top)
    self.assertTrue(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertIsNone(tag3.parent)
    self.assertEqual(tag3.child.id, tag1.id)
    self.assertTrue(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag1.id)
    self.assertEqual(tag4.child.id, tag2.id)
    self.assertFalse(tag4.is_top)
    self.assertFalse(tag4.is_buttom)
# ------------------------------- move tag2 up ------------------------------ #
    # tag3
    # tag1
    # tag2
    # tag4

    tag2 = UserPermissionTag.objects.get(tag_name="t2")

    UserPermissionTag.move_up(tag2)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertEqual(tag1.parent.id, tag3.id)
    self.assertEqual(tag1.child.id, tag2.id)
    self.assertFalse(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag1.id)
    self.assertEqual(tag2.child.id, tag4.id)
    self.assertFalse(tag2.is_top)
    self.assertFalse(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertIsNone(tag3.parent)
    self.assertEqual(tag3.child.id, tag1.id)
    self.assertTrue(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag2.id)
    self.assertIsNone(tag4.child)
    self.assertFalse(tag4.is_top)
    self.assertTrue(tag4.is_buttom)
# ------------------------------- move tag1 up ------------------------------ #
    # tag1
    # tag3
    # tag2
    # tag4

    tag1 = UserPermissionTag.objects.get(tag_name="t1")

    UserPermissionTag.move_up(tag1)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag3.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag3.id)
    self.assertEqual(tag2.child.id, tag4.id)
    self.assertFalse(tag2.is_top)
    self.assertFalse(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag1.id)
    self.assertEqual(tag3.child.id, tag2.id)
    self.assertFalse(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag2.id)
    self.assertIsNone(tag4.child)
    self.assertFalse(tag4.is_top)
    self.assertTrue(tag4.is_buttom)
# ------------------------------- move tag2 up ------------------------------ #
    # tag1
    # tag2
    # tag3
    # tag4

    tag2 = UserPermissionTag.objects.get(tag_name="t2")

    UserPermissionTag.move_up(tag2)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag2.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag1.id)
    self.assertEqual(tag2.child.id, tag3.id)
    self.assertFalse(tag2.is_top)
    self.assertFalse(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag2.id)
    self.assertEqual(tag3.child.id, tag4.id)
    self.assertFalse(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag3.id)
    self.assertIsNone(tag4.child)
    self.assertFalse(tag4.is_top)
    self.assertTrue(tag4.is_buttom)

  def test_move_down_tags(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    # ------------------------------- move tag4 down ------------------------------ #
    # tag3
    # tag1
    # tag4
    # tag2

    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    UserPermissionTag.move_down(tag4)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertEqual(tag1.parent.id, tag3.id)
    self.assertEqual(tag1.child.id, tag4.id)
    self.assertFalse(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag4.id)
    self.assertIsNone(tag2.child)
    self.assertFalse(tag2.is_top)
    self.assertTrue(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertIsNone(tag3.parent)
    self.assertEqual(tag3.child.id, tag1.id)
    self.assertTrue(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag1.id)
    self.assertEqual(tag4.child.id, tag2.id)
    self.assertFalse(tag4.is_top)
    self.assertFalse(tag4.is_buttom)
# ------------------------------- move tag3 down ------------------------------ #
    # tag1
    # tag3
    # tag4
    # tag2

    tag3 = UserPermissionTag.objects.get(tag_name="t3")

    UserPermissionTag.move_down(tag3)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag3.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag4.id)
    self.assertIsNone(tag2.child)
    self.assertFalse(tag2.is_top)
    self.assertTrue(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag1.id)
    self.assertEqual(tag3.child.id, tag4.id)
    self.assertFalse(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag3.id)
    self.assertEqual(tag4.child.id, tag2.id)
    self.assertFalse(tag4.is_top)
    self.assertFalse(tag4.is_buttom)
# ------------------------------- move tag4 down ------------------------------ #
    # tag1
    # tag3
    # tag2
    # tag4

    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    UserPermissionTag.move_down(tag4)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag3.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag3.id)
    self.assertEqual(tag2.child.id, tag4.id)
    self.assertFalse(tag2.is_top)
    self.assertFalse(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag1.id)
    self.assertEqual(tag3.child.id, tag2.id)
    self.assertFalse(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag2.id)
    self.assertIsNone(tag4.child)
    self.assertFalse(tag4.is_top)
    self.assertTrue(tag4.is_buttom)
# ------------------------------- move tag3 down ------------------------------ #
    # tag1
    # tag2
    # tag3
    # tag4

    tag3 = UserPermissionTag.objects.get(tag_name="t3")

    UserPermissionTag.move_down(tag3)

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

# ----------------------------------- tag1 ----------------------------------- #
    self.assertIsNone(tag1.parent)
    self.assertEqual(tag1.child.id, tag2.id)
    self.assertTrue(tag1.is_top)
    self.assertFalse(tag1.is_buttom)
# ----------------------------------- tag2 ----------------------------------- #
    self.assertEqual(tag2.parent.id, tag1.id)
    self.assertEqual(tag2.child.id, tag3.id)
    self.assertFalse(tag2.is_top)
    self.assertFalse(tag2.is_buttom)
# ----------------------------------- tag3 ----------------------------------- #
    self.assertEqual(tag3.parent.id, tag2.id)
    self.assertEqual(tag3.child.id, tag4.id)
    self.assertFalse(tag3.is_top)
    self.assertFalse(tag3.is_buttom)
# ----------------------------------- tag4 ----------------------------------- #
    self.assertEqual(tag4.parent.id, tag3.id)
    self.assertIsNone(tag4.child)
    self.assertFalse(tag4.is_top)
    self.assertTrue(tag4.is_buttom)

  def test_get_sorted_tags(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    tags = UserPermissionTag.get_sorted_tags()

    self.assertEqual(tags[0].tag_name, "t3")
    self.assertEqual(tags[1].tag_name, "t4")
    self.assertEqual(tags[2].tag_name, "t1")
    self.assertEqual(tags[3].tag_name, "t2")

  def test_update_hierarchy(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    tags = [tag3, tag1, tag4, tag2]

    UserPermissionTag.update_hierarchy(tags)

    tags = UserPermissionTag.get_sorted_tags()

    self.assertEqual(tags[0], tag3)
    self.assertEqual(tags[1], tag1)
    self.assertEqual(tags[2], tag4)
    self.assertEqual(tags[3], tag2)

  def test_update_hierarchy_invalid_hierarchy(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()
    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    # Define an invalid hierarchy with duplicate tags
    invalid_hierarchy = [tag1, tag2, tag1, tag3]

    # Try to update the hierarchy with the invalid hierarchy
    with self.assertRaises(Exception):
      UserPermissionTag.update_hierarchy(invalid_hierarchy)

  def test_update_hierarchy_first_last_tags_changed(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()
    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag3 = UserPermissionTag.objects.get(tag_name="t3")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    # Define a new hierarchy with changed first and last tags
    new_hierarchy = [tag1, tag2, tag3, tag4]

    # Try to update the hierarchy with changed first and last tags
    with self.assertRaises(Exception):
      UserPermissionTag.update_hierarchy(new_hierarchy)

  def test_update_hierarchy_different_length(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()
    tag1 = UserPermissionTag.objects.get(tag_name="t1")
    tag2 = UserPermissionTag.objects.get(tag_name="t2")

    # Define a new hierarchy with a different length
    new_hierarchy = [tag1, tag2]

    # Try to update the hierarchy with a different length
    with self.assertRaises(Exception):
      UserPermissionTag.update_hierarchy(new_hierarchy)

  def test_add_permission(self):
    # setUp_addPermission returns a tag and a permission
    tag, permission = self.setUp_addPermission()
    # Check that the tag initially has no permissions
    self.assertEqual(tag.permissions.count(), 0)

    # Add a permission to the tag
    tag.add_permission(permission.codename)

    # Check that the permission is added to the tag
    self.assertEqual(tag.permissions.count(), 1)

    # Check that the added permission is the same as the test permission
    added_permission = tag.permissions.first()
    self.assertEqual(added_permission, permission)

  def test_add_permission_nonexistent(self):
    # setUp_addPermission returns a tag and a permission
    tag, _ = self.setUp_addPermission()

    # Try to add a non-existent permission to the tag
    with self.assertRaises(Exception) as context:
      tag.add_permission("nonexistent_permission")

    # Check that an exception is raised
    self.assertTrue("Permission does not exist." in str(context.exception))

  def test_has_permission_true(self):
    # setUp_addPermission returns a tag and a permission
    tag, permission = self.setUp_addPermission()

    # Add a permission to the tag
    tag.add_permission(permission.codename)

    # Check that the tag has the permission
    self.assertTrue(tag.has_permission(permission.codename))

  def test_has_permission_false(self):
    # setUp_addPermission returns a tag and a permission
    tag, permission = self.setUp_addPermission()

    # Check that the tag does not have the permission
    self.assertFalse(tag.has_permission(permission.codename))

  def test_get_highest_tag(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()
    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    # Create a list of UserPermissionTags
    tags = [tag2, tag4]

    # Get the highest permission tag from the list
    highest_permission_tag = UserPermissionTag.get_highest_tag(tags)

    # Assert that the highest permission tag is the expected one
    self.assertEqual(highest_permission_tag, tag4)

  def test_get_highest_tag_with_one_tag(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()
    tag2 = UserPermissionTag.objects.get(tag_name="t2")

    # Create a list of UserPermissionTags that don't match the hierarchy
    tags = [tag2]

    # Get the highest permission tag from the list
    highest_permission_tag = UserPermissionTag.get_highest_tag(tags)

    # Assert that there is no match and the result is None
    self.assertEqual(highest_permission_tag, tag2)

  def test_get_highest_tag_empty_list(self):
    UserPermissionTagTestCase.create4Tags()

    # Create an empty list of UserPermissionTags
    tags = []

    # Get the highest permission tag from the empty list
    highest_permission_tag = UserPermissionTag.get_highest_tag(tags)

    # Assert that the result is None for an empty list
    self.assertIsNone(highest_permission_tag)

  def test_get_highest_tag_with_order(self):
    # tag3
    # tag4
    # tag1
    # tag2

    UserPermissionTagTestCase.create4Tags()

    tag2 = UserPermissionTag.objects.get(tag_name="t2")
    tag4 = UserPermissionTag.objects.get(tag_name="t4")

    # Create a list of UserPermissionTags
    tags = [tag2, tag4]

    highest_tag, top_order = UserPermissionTag.get_highest_tag(
        tags, return_order=True)

    self.assertEqual(highest_tag, tag4)
    self.assertEqual(top_order, 1)

    tags = [tag2]
    highest_tag, top_order = UserPermissionTag.get_highest_tag(
        tags, return_order=True)
    self.assertEqual(highest_tag, tag2)
    self.assertEqual(top_order, 3)

  def create4Tags():
    tag1 = UserPermissionTag.objects.create(tag_name="t1")
    UserPermissionTag.insert_tag(tag1)
    tag2 = UserPermissionTag.objects.create(tag_name="t2")
    UserPermissionTag.insert_tag(tag2, tag1.id)
    tag3 = UserPermissionTag.objects.create(tag_name="t3")
    UserPermissionTag.insert_tag(tag3)
    tag4 = UserPermissionTag.objects.create(tag_name="t4")
    UserPermissionTag.insert_tag(tag4, tag3.id)

  def setUp_addPermission(self):
    # get the content type for userPermissionTag model
    content_type = ContentType.objects.get_for_model(UserPermissionTag)
    # Create a test permission
    permission = Permission.objects.create(
        codename="test_permission", name="Test Permission", content_type=content_type,)

    # Create a test UserPermissionTag
    tag = UserPermissionTag.objects.create(
        tag_name="Test Tag")

    return tag, permission
