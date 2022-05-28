from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.views import View
from django.views.generic import ListView
from .models import Entry
# Create your views here.

def dummy_view(request, id):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now} and the id is {id}</body></html>"  
    return HttpResponse(html)

def status_code_view(request, exception):
    return HttpResponseNotFound('Pagina Web no encontrada, error 404')

def entry_list(request):
    return render(request, "posts/post_list.html", {})

def redirect_back_home(request):
    return redirect('/entries/1')

class MyClassView(View):
    def get(self, request):
        print("correr codigo")
        return HttpResponse("Response from a CBV")

class MyListView(ListView):
    model = Entry