import os
import profile
import uuid
from operator import ge
from urllib import response

from cv2 import log
from django.contrib.auth.models import User
from django.core.paginator import Page
from django.test import TestCase, tag
from django.urls import reverse

import users
from users import admin
from users.models import Profile, UserPermissionTag


class ProfileCRUDViewsTestCase(TestCase):
  basePath = os.path.dirname(__file__) + '/fixtures'
  # List the fixture file paths here
  fixtures = [f'{basePath}/UserPermissionTagData.json',
              f'{basePath}/UserData.json',
              f'{basePath}/AddressData.json',
              f'{basePath}/TalmzaLevelData.json',
              f'{basePath}/SchoolLevelData.json',
              f'{basePath}/ProfileData.json',
              ]

  def setUp(self):
    self.loggedInUser = User.objects.create_user(
        username='testuser1', password='testpassword')
    self.loggedInProfile = Profile.objects.create(
        user=self.loggedInUser, name='Test1 User test user', gender='M', birthdate='1995-01-01')
    self.adminTag = UserPermissionTag.objects.get(tag_name='admin')
    self.loggedInProfile.user_permission_tags.add(self.adminTag)
    # sign in as a user
    self.signIn(self.loggedInUser.username, 'testpassword')

    self.user1 = User.objects.create_user(
        username='testuser2', password='testpassword')
    self.profile1 = Profile.objects.create(
        user=self.user1, name='Test2 User test user', gender='M', birthdate='1990-05-05')
    self.tag3 = UserPermissionTag.objects.get(tag_name='tag3')
    self.profile1.user_permission_tags.add(self.tag3)
    self.profile1.save()

    self.user2 = User.objects.create_user(
        username='testuser3', password='testpassword')
    self.profile2 = Profile.objects.create(
        user=self.user2, name='Test3 User test user', gender='F', birthdate='2005-05-30')
    self.tag2 = UserPermissionTag.objects.get(tag_name='tag2')
    self.profile2.user_permission_tags.add(self.tag2)
    self.profile2.save()

  def signIn(self, username, password):
    # check if the user is already signed in
    if self.client.session.get('_auth_user_id') == str(self.loggedInUser.id):
      self.logout()

    # sign in as the user
    self.client.login(username=username, password=password)
    self.loggedInUser = User.objects.get(username=username)
    self.loggedInProfile = Profile.objects.get(user=self.loggedInUser)

  def logout(self):
    self.client.logout()

  def test_search_users_with_results(self):
    # Simulate a GET request with a search query
    response = self.client.get(reverse('search_users') + '?q=Test')
    # Check the response status code (200 OK)
    self.assertEqual(response.status_code, 200)

    # format the response data as json
    data = response.json()

    # Check if the query parameter is passed to the context
    self.assertEqual(data['query'], 'Test')

    # check if one of data['users'] is the profile we created
    self.assertTrue(any(
        uuid.UUID(profile['id']) == self.profile1.id for profile in data['users']))

  def test_search_users_no_results(self):
    # Simulate a GET request with a search query that has no results
    response = self.client.get(reverse('search_users') + '?q=NonExistent')

    # Check the response status code (200 OK)
    self.assertEqual(response.status_code, 200)

    # format the response data as json
    data = response.json()

    # Check if the query parameter is passed to the context
    self.assertEqual(data['query'], 'NonExistent')

    # check if the users list is empty
    self.assertEqual(len(data['users']), 0)

  def test_search_users_empty_query(self):
    # Simulate a GET request with an empty search query
    response = self.client.get(reverse('search_users') + '?q=')

    # Check the response status code (200 OK)
    self.assertEqual(response.status_code, 200)

    # format the response data as json
    data = response.json()

    # Check if the query parameter is an empty string in the context
    self.assertEqual(data['query'], '')

    # get the count of all profiles
    profiles_count = Profile.objects.all().count()

    # check if the users list contains all profiles
    self.assertTrue(0 < len(data['users']) <= profiles_count)

  def test_search_users_with_age_filter(self):
    # Test searching users with an age filter
    response = self.client.get(reverse('search_users'), {'age': '20-30'})

    # Check the response status code (200 OK)
    self.assertEqual(response.status_code, 200)

    # format the response data as json
    data = response.json()

    # check if the users list is not empty
    self.assertTrue(data['users'])

    # check if all users are in the age range
    for user in data['users']:
      self.assertTrue(20 <= user['age'] <= 30)

  def test_search_users_with_gender_filter(self):
    # Test searching users with a gender filter
    response = self.client.get(reverse('search_users'), {'gender': 'M'})
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertTrue(data['users'])

    for user in data['users']:
      self.assertTrue(user['gender'] == 'M')

  def test_search_users_with_highest_tag_filter(self):
    # Test searching users with a highest tag filter
    response = self.client.get(reverse('search_users'), {
                               'highest_tag': 'مخدوم'})
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertTrue(data['users'])

    tag = UserPermissionTag.objects.get(tag_name='مخدوم')
    for user in data['users']:
      self.assertTrue(user['highest_tag__tag_name'] == tag.tag_name)

  def test_search_users_pagination(self):
      # Test pagination by requesting a specific page number
    response = self.client.get(reverse('search_users'), {'page': 10})
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertTrue(isinstance(data['users'], list))
    self.assertIsInstance(data['current_page'], int)
    self.assertIsInstance(data['total_pages'], int)

  def test_search_users_with_filters(self):
    # Test searching for users with filters and getting specific attributes
    response = self.client.get(reverse('search_users'), {
        'q': 'Test',
        'age': '30-40',
        'gender': 'M',
        'highest_tag': 'tag3'
    })

    # Check the response status code (200 OK)
    self.assertEqual(response.status_code, 200)

    # Parse the response data as JSON
    data = response.json()

    # Ensure that 'users' in the response data is a list
    self.assertIsInstance(data['users'], list)

    # Check that 'current_page' and 'total_pages' are integers
    self.assertIsInstance(data['current_page'], int)
    self.assertIsInstance(data['total_pages'], int)

    # Check that the search results match the applied filters
    tag3 = UserPermissionTag.objects.get(tag_name='tag3')

    self.assertEqual(len(data['users']), 1)
    for user_data in data['users']:
      user = Profile.objects.get(id=user_data['id'])
      self.assertIn('Test2', user_data['name'])  # Name contains 'User'
      self.assertTrue(30 <= user.age <= 40)  # Age is between 30 and 40
      self.assertEqual(user.gender, 'M')  # Gender is 'M'
      self.assertEqual(user_data['highest_tag__tag_name'], tag3.tag_name)

  def test_search_users_with_profile2_logged_in(self):
    # this test to check that user with tag higher than tag2 won't appear in the search result
    self.signIn(self.user2.username, 'testpassword')
    response = self.client.get(reverse('search_users'), {'q': 'Test'})
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertTrue(data['users'])

    tag2 = UserPermissionTag.objects.get(tag_name='tag2')
    adminTag = UserPermissionTag.objects.get(tag_name='admin')
    for user in data['users']:
      self.assertTrue(user['highest_tag__tag_name'] != tag2.tag_name)
      self.assertTrue(user['highest_tag__tag_name'] != adminTag.tag_name)

  def test_get_user_profile(self):
    # Test getting a user's profile
    tempProfile = Profile.objects.get(name='صموئيل سعد فكري سعد')
    response = self.client.get(
        reverse('get_user_profile', args=[tempProfile.id]))
    self.assertEqual(response.status_code, 200)
    data = response.json()
    self.assertEqual(data['user']['name'], tempProfile.name)
