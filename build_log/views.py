from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """The homepage for the build log"""
    return render(request, 'build_log/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')  # add topics into list ordered by date
    context = {'topics': topics}   # set the context name for this list to be accessed in html
    return render(request, 'build_log/topics.html', context) # pass back template and context

