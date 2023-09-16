from users.models import Profile, UserPermissionTag
from utils.run_test import runTest


def test():
  runTest('users', 'ProfileCRUDViewsTestCase', 'test_get_user_profile')
  # runTest('users')


# test()
