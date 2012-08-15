#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
import datetime
import logging
from constants import *

logger = logging.getLogger(__name__)

from buscape import Buscape

from settings import BUSCAPE_APP_ID

def index(request):
    
    return render_to_response(INDEX_HTML, dict(cloud_list=CloudTag.objects.all()))

def quero_fazer(request):
    
    buscape = Buscape(BUSCAPE_APP_ID)

    searchWord = request.POST[SEARCH_PARAM]

    productService = ProductService.objects(name=searchWord).first()

    for item in productService.items :
        
        logger.info(u"Querying Buscapé for %s" % item.name)
        offer = buscape.find_offer_list(keyword=item.name).offer[0].offer

        item.price = offer.price.value
        item.thumbnail = offer.thumbnail.url
        item.seller = offer.seller.sellername
    
    return render_to_response(EDIT_HTML, dict(productService=productService))
