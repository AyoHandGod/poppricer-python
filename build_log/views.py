from django.shortcuts import render

# Create your views here.
def index(request):
    """The homepage for the build log"""
    return render(request, 'build_log/index.html')