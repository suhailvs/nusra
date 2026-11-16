Setup
1. Copy this folder into your Django project as an app named "tracker".
2. settings.py  -> INSTALLED_APPS += ["tracker"]
3. project urls.py -> path("", include("tracker.urls"))
4. python manage.py makemigrations tracker && python manage.py migrate
