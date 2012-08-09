from django.shortcuts import render_to_response
from django.template import RequestContext
from models import CloudTag
import datetime

def index(request):
    
    return render_to_response('index.html', dict(cloud_list=CloudTag.objects.all()))

def quero_fazer(request):
    
    
    
    return render_to_response('edit.html')
