from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import datetime


@require_http_methods(["GET"], )
def get_current_server_time(request):
    return HttpResponse(datetime.datetime.now())