from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *

from .models import Pop, Character


# Create your views here.
def search(request):
    return render(request, 'pricer/search.html')


def search_result(request):
    if request.method == 'POST':
        search_target = request.POST.get('search_field', None)
        try:
            character = Character.objects.get(name=search_target)
            html = ("<H1>Lucky Find</H1>")

        except ObjectDoesNotExist:
            return HttpResponse("No character found")
    else:
        return render(request, 'pricer/search.html')