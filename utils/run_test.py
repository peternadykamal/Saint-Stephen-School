from django.test.runner import DiscoverRunner


def runTest(app, test_case_class_name=None, test_method=None):
  if not app:
    return
  print(
      f'# ------------------------------------ testing: {app} ----------------------------------- #')
  test_runner = DiscoverRunner(verbosity=0)
  formatted_path = app
  if test_case_class_name:
    formatted_path += f'.tests.{test_case_class_name}'
    if test_method:
      formatted_path += f'.{test_method}'

  failures = test_runner.run_tests([formatted_path])
  print('# --------------------------------------------------------------------------------------- #')
