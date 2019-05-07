from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *

from .models import Pop, Character
from .web.web import *


# Create your views here.
# Search form page
def search(request):
    """
    Search form page view
    :param request:  Http Request received.
    :return: html template to render pricer/search.html
    """
    return render(request, 'pricer/search.html')

# Handles search button functionality
def search_result(request):
    """
    Search result page view
    :param request: POST request received via button on search page.
        Use search_field data
    :return: HttpResponse depending on results
    """
    if request.method == 'GET':
        search_target = request.GET.get('search_field', None)
        try:
            character = Character.objects.get(name=str(search_target))
            pops = Pop.objects.filter(character=character)
            html = ("<H1>Lucky Find: {}</H1>".format(character.name))
            return HttpResponse(html)

        except ObjectDoesNotExist:
            pops = ppgWebQuery(str(search_target))
            if pops is not None:
                addPopListToDB(pops)
                # context = Pop.objects.get(character=search_target)
                return HttpResponse("Awww yeah! ")
            return HttpResponse("No character found")
    else:
        return render(request, 'pricer/search.html')