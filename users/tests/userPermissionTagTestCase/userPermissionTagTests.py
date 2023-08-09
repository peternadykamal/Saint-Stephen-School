from django.test import TestCase
# Replace "your_app" with the actual name of your app
from users.models import UserPermissionTag, Profile

import os


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

  def create4Tags():
    tag1 = UserPermissionTag.objects.create(tag_name="t1")
    UserPermissionTag.insert_tag(tag1)
    tag2 = UserPermissionTag.objects.create(tag_name="t2")
    UserPermissionTag.insert_tag(tag2, tag1.id)
    tag3 = UserPermissionTag.objects.create(tag_name="t3")
    UserPermissionTag.insert_tag(tag3)
    tag4 = UserPermissionTag.objects.create(tag_name="t4")
    UserPermissionTag.insert_tag(tag4, tag3.id)
