from django.utils.deprecation import MiddlewareMixin

class CustomSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin'):
            request.session.modified = True
            request.session.save()
        else:
            request.session.modified = False
