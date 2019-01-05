# django-malice

django-malice is a simple Django app that provides an easy and simple View Error(403, 404, 500) and 200 OK Testing for develop and production environment.

# Feature
- It can cause an 403, 404, 500 error.

# Dependencies
- python 3
- django >= 1.11

# Quick start

1. Install django-malice

```
pip install django-malice
```

2. Add "malice" to your INSTALLED_APPS setting like this:

```
INSTALLED_APPS = [
    ...
    'malice',
]
```

3. Include the malice URLconf in your project urls.py like this:

```
url(r'^malice/', include('malice.urls', namespace='malice')),
```

4. Run runserver and open below url

```
./manage.py runserver 0.0.0.0:8000
```

-  http://localhost:8000/malice/200
-  http://localhost:8000/malice/404
-  http://localhost:8000/malice/403
-  http://localhost:8000/malice/500
