from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
import datetime

from buscape import Buscape

from settings import BUSCAPE_APP_ID

def index(request):
    
    return render_to_response('index.html', dict(cloud_list=CloudTag.objects.all()))

def quero_fazer(request):
    
    buscape = Buscape(BUSCAPE_APP_ID)

    searchWord = request.POST['search']

    productService = ProductService.objects(name=searchWord).first()

    for item in productService.items :
        
        offer = buscape.find_offer_list(keyword=item.name)['data']['offer'][0]['offer']

        item.price = offer['price']['value']
        item.thumbnail =  offer['thumbnail']['url']
        item.seller = offer['seller']['sellername']
    
    return render_to_response('edit.html', dict(items=productService.items,name=productService.name))
