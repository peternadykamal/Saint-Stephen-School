#!/bin/bash

# Message function to display step information
show_message() {
    echo "=== $1 ==="
}

# Activate virtual environment
show_message "Activating virtual environment"
source env/bin/activate

# Get the parent directory of the virtual environment folder
workspace_dir=$(dirname "$VIRTUAL_ENV")

# Get the directory where the script is located
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
nginx_config="$script_dir/nginx.conf"

# Set up cleanup function
cleanup() {
    echo "=== Cleaning up... ==="
    sudo nginx -c "$nginx_config" -p "$workspace_dir" -s quit
    kill -TERM "$gunicorn_pid" 2>/dev/null
}

# Find default gateway address
show_message "Finding default gateway address"
gate_test=$(ip route | grep default | awk '{print $3}')
range=$(echo $gate_test | cut -d. -f1-3)

# Find local IP address in the same range
ipaddress=$(ip addr | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}' | cut -d/ -f1 | grep $range)

echo "My IP Address is $ipaddress"

# Run collectstatic
show_message "Running collectstatic"
python manage.py collectstatic --noinput

# Run the server with the dynamic IP in the background
show_message "Starting gunicorn server"
gunicorn -c "$(dirname "$0")/gunicorn_config.py" Saint_Stephen_School.wsgi:application --bind $ipaddress:8000 &
gunicorn_pid=$!

# Set trap for cleanup on script exit
trap cleanup EXIT

# Start Nginx
show_message "Starting Nginx"
sudo nginx -c "$nginx_config" -p "$workspace_dir"

# Wait for background processes to finish
wait
