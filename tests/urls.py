try:
    from django.urls import url, include
except:
    from django.conf.urls import url, include

from django.contrib import admin


app_name = 'malice'

urlpatterns = [
    url(
        r'^malice/', include(
            'malice.urls',
            namespace='malice',
        )
    ),
]
