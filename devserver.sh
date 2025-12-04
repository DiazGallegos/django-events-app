#!/bin/sh

# Terminate any existing Django development server processes
ps aux | grep 'manage.py runserver' | grep -v grep | awk '{print $2}' | xargs kill -9

# Activate the virtual environment
source .venv/bin/activate

# Start the Django development server
python mysite/manage.py runserver $PORT
