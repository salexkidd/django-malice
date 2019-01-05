"""
The MIT License (MIT)

Copyright (c) 2015 bpyamasinn.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from django.views import View
from django.conf import settings
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied as _PermissionDenied


def if_admin_only(func):

    def wrapper(self, request, *args, **kwargs):

        if getattr(settings, "MALICE_ADMIN_ONLY", True):
            if not request.user.is_superuser:
                raise Http404

        return func(request, *args, **kwargs)

    return wrapper


class OK(View):

    @if_admin_only
    def get(self, *args, **kwargs):
        return HttpResponse("I'm OK", status=200)


class PermissionDenied(View):

    @if_admin_only
    def get(self, *args, **kwargs):
        raise _PermissionDenied("It is Error with a malicious! (403 Forbidden)")


class NotFound(View):

    @if_admin_only
    def get(self, *args, **kwargs):
        raise Http404("It is Error with a malicious! (404 Not Found)")


class InternalServerError(View):

    @if_admin_only
    def get(self, *args, **kwargs):
        raise ValueError("It is Error with a malicious! (500 Internal Server Error)")
