#!/bin/bash
pip install -r requirements.txt
python manage.py migrate || echo "migrate failed"
