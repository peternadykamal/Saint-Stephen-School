workers = 1  # Number of worker processes

# Logging configuration
accesslog = 'deployLogs/gunicorn_access.log'
errorlog = 'deployLogs/gunicorn_error.log'

# Worker settings
worker_class = 'sync'  # Use synchronous workers
worker_connections = 250  # Maximum number of simultaneous connections

# Other settings
# the maximum amount of time (in seconds) a worker process is allowed to spend processing a request
timeout = 30
