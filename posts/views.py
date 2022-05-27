from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import datetime
# Create your views here.

def dummy_view(request):
    now = datetime.datetime.now()
    html = '<html><body> It is now %s</body></html>' % now
    return HttpResponse(hmtl)

def status_code_view(request, exception):
    return HttpResponseNotFound('Pagina Web no encontrada, error 404')