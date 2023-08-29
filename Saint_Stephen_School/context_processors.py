
def navigation_config(request):
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
  NAVIGATION_CONFIG = [
      {'type': 'link', 'label': 'استمارة التقديم', 'url': "profile-form"},
      {'type': 'link', 'label': "تعديل شعارات", 'url': "tag-page"},
  ]
  return {'nav_items': NAVIGATION_CONFIG}
