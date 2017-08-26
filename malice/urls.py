from django.conf.urls import url

from . import views as malice_views


urlpatterns = [

    url(
        r'^200/$',
        malice_views.OK.as_view(),
        name="ok"
    ),

    url(
        r'^403/$',
        malice_views.PermissionDenied.as_view(),
        name="permission-denied"
    ),

    url(
        r'^404/$',
        malice_views.NotFound.as_view(),
        name="not-found"
    ),

    url(
        r'^500/$',
        malice_views.InternalServerError.as_view(),
        name="internal-server-error"
    ),

]
