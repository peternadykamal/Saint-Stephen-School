
import profile


def generate_navigation_items(permissions, tags, items):
  navigation_items = []

  for item in items:
    # Check if the user has the specified permission or if it's a dropdown (inherit permissions)
    if (
        item.get('type') == 'dropdown' or
        item.get('permission') in [
            p.codename for p in permissions] or
        item.get('tag') in [t.tag_name for t in tags]
    ):
      if item.get('type') == 'dropdown':
        # If it's a dropdown, recursively generate sub-items
        sub_items = generate_navigation_items(
            permissions, tags, item.get('items', []))
        # check if dropdown has no permission and no tag or has the required permission or tag
        if (
            # Include the item in the navigation if any of the following conditions is True:
            # 1. The item has a permission but no tag (permission XOR tag)
            (item.get('permission') and not item.get('tag')) or
            # 2. The item has a tag but no permission (tag XOR permission)
            (item.get('tag') and not item.get('permission')) or
            # 3. The item's permission is in the user's permissions
            (item.get('permission') in [p.codename for p in permissions]) or
            # 4. The item's tag is in the user's tags
            (item.get('tag') in [t.tag_name for t in tags])
        ):
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
  #         {'tag': 'admin', 'type': 'link',
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
      {'tag': 'admin', 'type': 'link',
       'label': "تعديل شعارات", 'url': "tag-page"},
  ]

  NAVIGATION_CONFIG = []
  # check if user is authenticated
  if request.user.is_authenticated:
    profilePermissions = request.profile.getAllPermissions()
    profileTags = request.profile.user_permission_tags.all()
  else:
    profilePermissions = []
    profileTags = []
  NAVIGATION_CONFIG.extend(
      (generate_navigation_items(profilePermissions, profileTags, navigation_items)))

  return {'nav_items': NAVIGATION_CONFIG, 'permissions': [p.codename for p in profilePermissions]}
