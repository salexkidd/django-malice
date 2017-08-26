from django.views import View
from django.http import HttpResponse, Http404

from django.core.exceptions import PermissionDenied as _PermissionDenied


class OK(View):
    def get(self, *args, **kwargs):
        return HttpResponse("I'm good guy", status=200)


class PermissionDenied(View):
    def get(self, *args, **kwargs):
        raise _PermissionDenied("It is Error with a malicious!(403)")


class NotFound(View):
    def get(self, *args, **kwargs):
        raise Http404("It is Error with a malicious!(404)")


class InternalServerError(View):
    def get(self, *args, **kwargs):
        raise ValueError("It is Error with a malicious!(500)")
