from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('Hello From')
    return render(request, 'it_blog/index.html')


