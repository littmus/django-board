# -*- coding: utf-8 -*-

from django.http import HttpResponse


def HttpErrorResponse(error);
    return HttpResponse('<script>alert("%s");history.go(-1);</script>' % error)


