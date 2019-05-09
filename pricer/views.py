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
            pops = Pop.objects.filter(character=character).order_by('-value')
            context = {"character_name": character.name, "pops": pops}
            return render(request, 'pricer/searchResult.html', context)

        except ObjectDoesNotExist:
            poplist = ppgWebQuery(str(search_target))
            if poplist is not None:
                addPopListToDB(poplist)
                character = Character.objects.get(name=str(search_target))
                pops = Pop.objects.filter(character=character).order_by('-value')
                context = {"character_name": character.name, "pops": pops}
                return render(request, 'pricer/searchResult.html', context)

            return HttpResponse("No character found")

    else:
        return render(request, 'pricer/search.html')