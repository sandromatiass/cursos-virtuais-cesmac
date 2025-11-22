#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

# Create necessary directories
mkdir -p staticfiles

echo "Build completed successfully!"