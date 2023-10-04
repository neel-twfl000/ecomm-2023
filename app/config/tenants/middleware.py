import threading
from django.shortcuts import HttpResponse, redirect
from .utils import tenant_db_from_the_request

Thread_Local = threading.local()

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_the_request(request)
        print(db, '------>>>')
        if db:

            setattr(Thread_Local, "DB", db)
            response = self.get_response(request)
            return response
        return HttpResponse("Not Found!")
    
def get_current_db_name():
    return getattr(Thread_Local, "DB", None)