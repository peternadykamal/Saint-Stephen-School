import subprocess


def get_current_git_branch():
  try:
    return subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
  except subprocess.CalledProcessError:
    return None
