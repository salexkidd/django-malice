# django-malice

django-malice is a simple Django app that provides an easy and simple View Error(403, 404, 500) and 200 OK Testing for development and production environment.

# Feature
- It can cause an 403, 404, 500 error.

# Dependencies
- python 3.6, 3.7
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

And you want gets some malice's errors by not admin user, please set "MALICE_ADMIN_ONLY" is False

```
MALICE_ADMIN_ONLY = False
```


1. Include the malice URLconf in your project urls.py like this:

```
url(r'^malice/', include('malice.urls', namespace='malice')),

# or (django 2.0)

path('malice/', include('malice.urls', namespace='malice')),

```

If you don't want production envirionment, like this.

```
from django.conf import settings

if settings.DEBUG:
    urlpatterns += [
        url(r'^malice/', include('malice.urls', namespace='malice'))
    ]

# or (django 2.0)

if settings.DEBUG:
    urlpatterns += [
        path('malice/', include('malice.urls', namespace='malice'))
    ]

```

4. Run runserver and open below url

```
./manage.py runserver 0.0.0.0:8000
```

-  http://localhost:8000/malice/200
-  http://localhost:8000/malice/404
-  http://localhost:8000/malice/403
-  http://localhost:8000/malice/500

