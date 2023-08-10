from users.models import Profile


def test():
  profile = Profile.objects.get(name='شادي جرجس جرجس بخيت')
  # print(profile.getHighestPermissionTag())
  print(profile.getLowestPermissionTag())


# test()
