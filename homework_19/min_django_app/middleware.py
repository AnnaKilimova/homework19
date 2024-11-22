import logging
from django.utils.timezone import now
from django.shortcuts import render

logger = logging.getLogger(__name__)

class AccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/min_django_app/'):
            logger.info(f"Access attempt: {request.path} at {now()}")
        response = self.get_response(request)
        return response


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            return render(request, 'errors/500.html', status=500)
        if response.status_code == 404:
            return render(request, 'errors/404.html', status=404)
        return response

