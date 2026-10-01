#!/bin/bash
set -e
echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py migrate --noinput
python3.9 manage.py collectstatic --noinput --clear
cp index.html staticfiles_build/index.html
echo "BUILD END"
