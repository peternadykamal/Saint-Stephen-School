from django.test import TestCase
# Replace "your_app" with the actual name of your app
from users.models import Profile, TalmzaLevel


class ProfileTestCase(TestCase):
  # List the fixture file paths here
  fixtures = ['users/fixtures/ProfileData.json',
              'users/fixtures/UserData.json',
              'users/fixtures/AddressData.json',
              'users/fixtures/TalmzaLevelData.json',
              'users/fixtures/SchoolLevelData.json',
              ]

  def setUp(self):
    # Create a Profile object with some initial values
    self.profile1 = Profile.objects.get(user__username='2300008')
    self.profile2 = Profile.objects.get(user__username='2300009')
    self.profile3 = Profile.objects.get(user__username='2300012')
    self.profile4 = Profile.objects.get(user__username='2300013')

  def test_level_up_talmza(self):
    self.profile1TalmzaLevel = self.profile1.talmza_level
    self.profile2TalmzaLevel = self.profile2.talmza_level
    self.profile3TalmzaLevel = self.profile3.talmza_level

    # Call the levelUpTalmza method on the Profile object
    # talmza level تمهيدي year 1 will be year 2 in same level
    updated1 = self.profile1.levelUpTalmza()
    # talmza level تمهيدي year 2 will be year 1 in next level
    updated2 = self.profile2.levelUpTalmza()
    # talmza level الرابع year 2 can't level up
    updated3 = self.profile3.levelUpTalmza()

    self.assertTrue(updated1)
    self.assertTrue(updated2)
    self.assertFalse(updated3)

    # Get the updated profile from the database to check if the talmza_level and current_talmza_level_year were updated correctly
    updated_profile1 = Profile.objects.get(id=self.profile1.id)
    updated_profile2 = Profile.objects.get(id=self.profile2.id)
    updated_profile3 = Profile.objects.get(id=self.profile3.id)

    # Check if the talmza_level was updated correctly
    self.assertIsNotNone(updated_profile1.talmza_level)
    self.assertIsNotNone(updated_profile2.talmza_level)
    self.assertIsNotNone(updated_profile3.talmza_level)

    # Check if the current_talmza_level_year was updated correctly
    self.assertEqual(updated_profile1.current_talmza_level_year, 2)
    self.assertEqual(updated_profile1.talmza_level.id,
                     self.profile1TalmzaLevel.id)

    self.assertEqual(updated_profile2.current_talmza_level_year, 1)
    self.assertEqual(updated_profile2.talmza_level.id,
                     self.profile2TalmzaLevel.next_level.id)

    self.assertEqual(updated_profile3.current_talmza_level_year, 2)
    self.assertEqual(updated_profile3.talmza_level.id,
                     self.profile3.talmza_level.id)

  def test_level_down_talmza(self):
    self.profile1TalmzaLevel = self.profile1.talmza_level
    self.profile2TalmzaLevel = self.profile2.talmza_level
    self.profile4TalmzaLevel = self.profile4.talmza_level

    # Call the levelUpTalmza method on the Profile object
    # talmza level تمهيدي year 1 will be year 2 in Prevues level
    updated1 = self.profile1.levelDownTalmza()
    # talmza level تمهيدي year 2 will be year 1 in same level
    updated2 = self.profile2.levelDownTalmza()
    # talmza level اقل من تمهيدي year 1 can't level up
    updated4 = self.profile4.levelDownTalmza()

    self.assertTrue(updated1)
    self.assertTrue(updated2)
    self.assertFalse(updated4)

    # Get the updated profile from the database to check if the talmza_level and current_talmza_level_year were updated correctly
    updated_profile1 = Profile.objects.get(id=self.profile1.id)
    updated_profile2 = Profile.objects.get(id=self.profile2.id)
    updated_profile4 = Profile.objects.get(id=self.profile4.id)

    # Check if the talmza_level was updated correctly
    self.assertIsNotNone(updated_profile1.talmza_level)
    self.assertIsNotNone(updated_profile2.talmza_level)
    self.assertIsNotNone(updated_profile4.talmza_level)

    # Check if the current_talmza_level_year was updated correctly
    self.assertEqual(updated_profile1.current_talmza_level_year, 2)
    self.assertEqual(updated_profile1.talmza_level.id,
                     self.profile1TalmzaLevel.prevues_level.id)

    self.assertEqual(updated_profile2.current_talmza_level_year, 1)
    self.assertEqual(updated_profile2.talmza_level.id,
                     self.profile2TalmzaLevel.id)

    self.assertEqual(updated_profile4.current_talmza_level_year, 1)
    self.assertEqual(updated_profile4.talmza_level.id,
                     self.profile4.talmza_level.id)

  def test_level_up_school(self):
    self.profile1SchoolLevel = self.profile1.school_level
    self.profile2SchoolLevel = self.profile2.school_level
    self.profile3SchoolLevel = self.profile3.school_level

    # Call the levelUpSchool method on the Profile object
    # school level الابتدائي year 1 will be year 2 in same level
    updated1 = self.profile1.levelUpSchool()
    # school level الابتدائي year 2 will be year 1 in next level
    updated2 = self.profile2.levelUpSchool()
    # school level جمعة year 1 can't level up
    updated3 = self.profile3.levelUpSchool()

    self.assertTrue(updated1)
    self.assertTrue(updated2)
    self.assertFalse(updated3)

    # Get the updated profile from the database to check if the school_level and current_school_level_year were updated correctly
    updated_profile1 = Profile.objects.get(id=self.profile1.id)
    updated_profile2 = Profile.objects.get(id=self.profile2.id)
    updated_profile3 = Profile.objects.get(id=self.profile3.id)

    # Check if the school_level was updated correctly
    self.assertIsNotNone(updated_profile1.school_level)
    self.assertIsNotNone(updated_profile2.school_level)
    self.assertIsNotNone(updated_profile3.school_level)

    # Check if the current_school_level_year was updated correctly
    self.assertEqual(updated_profile1.current_school_level_year, 2)
    self.assertEqual(updated_profile1.school_level.id,
                     self.profile1SchoolLevel.id)

    self.assertEqual(updated_profile2.current_school_level_year, 1)
    self.assertEqual(updated_profile2.school_level.id,
                     self.profile2SchoolLevel.next_level.id)

    self.assertEqual(updated_profile3.current_school_level_year, 1)
    self.assertEqual(updated_profile3.school_level.id,
                     self.profile3.school_level.id)

  def test_level_down_school(self):
    self.profile1SchoolLevel = self.profile1.school_level
    self.profile2SchoolLevel = self.profile2.school_level
    self.profile4SchoolLevel = self.profile4.school_level

    # Call the levelUpSchool method on the Profile object
    # school level الابتدائي year 1 will be year 2 in Prevues level
    updated1 = self.profile1.levelDownSchool()
    # school level الابتدائي year 2 will be year 1 in same level
    updated2 = self.profile2.levelDownSchool()
    # school level اقل من حضانة year 1 can't level up
    updated4 = self.profile4.levelDownSchool()

    self.assertTrue(updated1)
    self.assertTrue(updated2)
    self.assertFalse(updated4)

    # Get the updated profile from the database to check if the school_level and current_school_level_year were updated correctly
    updated_profile1 = Profile.objects.get(id=self.profile1.id)
    updated_profile2 = Profile.objects.get(id=self.profile2.id)
    updated_profile4 = Profile.objects.get(id=self.profile4.id)

    # Check if the school_level was updated correctly
    self.assertIsNotNone(updated_profile1.school_level)
    self.assertIsNotNone(updated_profile2.school_level)
    self.assertIsNotNone(updated_profile4.school_level)

    # Check if the current_school_level_year was updated correctly
    self.assertEqual(updated_profile1.current_school_level_year, 2)
    self.assertEqual(updated_profile1.school_level.id,
                     self.profile1SchoolLevel.prevues_level.id)

    self.assertEqual(updated_profile2.current_school_level_year, 5)
    self.assertEqual(updated_profile2.school_level.id,
                     self.profile2SchoolLevel.id)

    self.assertEqual(updated_profile4.current_school_level_year, 1)
    self.assertEqual(updated_profile4.school_level.id,
                     self.profile4.school_level.id)
