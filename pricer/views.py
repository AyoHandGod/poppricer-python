from django.shortcuts import render
from .models import Pop

# Create your views here.
def search(request):
    return render(request, 'pricer/search.html')