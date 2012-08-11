from django.shortcuts import render_to_response
from django.template import RequestContext
from models import CloudTag
import datetime

from buscape import Buscape

from settings import BUSCAPE_APP_ID

def index(request):
    
    return render_to_response('index.html', dict(cloud_list=CloudTag.objects.all()))

def quero_fazer(request):
    
    busca = Buscape(BUSCAPE_APP_ID)

    result = busca.find_category_list(categoryID=77)
    
    return render_to_response('edit.html', dict(result=result))
