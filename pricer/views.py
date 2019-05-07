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
    if request.method == 'POST':
        search_target = request.POST.get('search_field', None)

        # try searching the database for a character with search_target name
        try:
            character = Character.objects.get(name=search_target)
            pops = Pop.objects.get(character=character)
            html = ("<H1>Lucky Find: {}</H1>".format(character.name))
            return HttpResponse(html)
        except ObjectDoesNotExist:
            # search ppg for the search_target
            pops = ppgWebQuery(search_target)

            # if pops are successfully found, add the to the DB and return the success response.
            if pops is not None:
                addPopListToDB(pops)
                # context = Pop.objects.get(character=search_target)
                return HttpResponse("Awww yeah! ")

            # if the results are 0
            return HttpResponse("No pops found for this search.")
    else:
        return render(request, 'pricer/search.html')