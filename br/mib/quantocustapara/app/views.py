from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post
import datetime

def index(request):
    return render_to_response('index.html')


