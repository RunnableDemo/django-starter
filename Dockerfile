FROM runnable/django-starter

# Add Repository
ADD . /app/

# Run Migrations & Server
CMD bash wait-for-postgres-then-run.sh python manage.py runserver 0.0.0.0:8000
