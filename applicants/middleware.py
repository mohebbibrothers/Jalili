from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponseNotFound

class Redirect404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response, HttpResponseNotFound):
            return redirect(settings.HOME_REDIRECT_URL)
        return response
