import logging

logger = logging.getLogger(__name__)

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request method: {request.method}, Request path: {request.path}")
        response = self.get_response(request)
        return response
