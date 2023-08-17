import os

workers = 1  # Number of worker processes

# Determine the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Set the paths based on the script directory
accesslog = os.path.join(script_dir, 'deployLogs/gunicorn_access.log')
errorlog = os.path.join(script_dir, 'deployLogs/gunicorn_error.log')

# Worker settings
worker_class = 'sync'  # Use synchronous workers
worker_connections = 250  # Maximum number of simultaneous connections

# Other settings
# the maximum amount of time (in seconds) a worker process is allowed to spend processing a request
timeout = 30

capture_output = True
