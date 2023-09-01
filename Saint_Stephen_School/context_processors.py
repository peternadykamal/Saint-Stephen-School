
import profile


def generate_navigation_items(permissions, items):
  navigation_items = []

  for item in items:
    # Check if the user has the specified permission or if it's a dropdown (inherit permissions)
    if (
        item.get('type') == 'dropdown' or
        item.get('permission') in [
            p.codename for p in permissions]
    ):
      if item.get('type') == 'dropdown':
        # If it's a dropdown, recursively generate sub-items
        sub_items = generate_navigation_items(
            permissions, item.get('items', []))
        # check if dropdown has no permission or if it has permission does it in the given permissions
        if not item.get('permission') or item.get('permission') in [p.codename for p in permissions]:
          # Include the dropdown item only if it has sub-items or no permissions specified
          if sub_items:
            item['items'] = sub_items
            navigation_items.append(item)
      else:
        # If it's a link and has the required permission, add it to navigation_items
        navigation_items.append({
            'type': 'link',
            'label': item['label'],
            'url': item['url'],
        })

  return navigation_items


def navigation_config(request):
  # here is an example of navigation items format that is used in the generate_navigation_items function
  # navigation_items = [
  #     {'permission': 'add_profile',
  #      'type': 'link', 'label': 'استمارة التقديم', 'url': "profile-form"},
  #     {'permission': 'change_userpermissiontag', 'type': 'link',
  #      'label': "تعديل شعارات", 'url': "tag-page"},
  #     {'permission': 'add_profile', 'type': 'dropdown', 'label': 'Dropdown 1', 'items': [
  #         {'permission': 'add_profile',
  #          'type': 'link', 'label': 'استمارة التقديم', 'url': "profile-form"},
  #         {'permission': 'change_userpermissiontag', 'type': 'link',
  #             'label': "تعديل شعارات", 'url': "tag-page"},
  #     ]},
  # ]

  # here is an example of a navigation config format
  # NAVIGATION_CONFIG = [
  #     {'type': 'link', 'label': "form", 'url': "profile-form"},
  #     {'type': 'link', 'label': "home", 'url': "landing"},
  #     {'type': 'dropdown', 'label': 'Dropdown 1', 'items': [
  #         {'type': 'link', 'label': 'form',
  #          'url': 'profile-form'},
  #         {'type': 'link', 'label': 'home',
  #          'url': 'landing'},
  #         {'type': 'divider', },
  #         {'type': 'link', 'label': 'sign in',
  #          'url': 'sign-in'},
  #     ]}
  # ]

  navigation_items = [
      {'permission': 'add_profile',
       'type': 'link', 'label': 'استمارة التقديم', 'url': "profile-form"},
      {'permission': 'change_userpermissiontag', 'type': 'link',
       'label': "تعديل شعارات", 'url': "tag-page"},
  ]

  NAVIGATION_CONFIG = []
  # check if user is authenticated
  if request.user.is_authenticated:
    profilePermissions = request.profile.getAllPermissions()
  else:
    profilePermissions = []
  NAVIGATION_CONFIG.extend(
      (generate_navigation_items(profilePermissions, navigation_items)))

  return {'nav_items': NAVIGATION_CONFIG, 'permissions': [p.codename for p in profilePermissions]}
