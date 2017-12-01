#!/usr/bin/env bash



python3 manage.py makemigrations app
python3 manage.py migrate
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')"
daphne -b 0.0.0.0 -p 80 -t 600  --proxy-headers app.asgi:channel_layer &
while true;do

    python3 manage.py runworker --threads 2 &
    PID=$!
    inotifywait --format='%f modified.  Reloading.' -e modify -r . --exclude='.*[^p][^y]$'
    kill $PID

done


