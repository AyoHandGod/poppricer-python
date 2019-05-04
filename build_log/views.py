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


def topic(request, topic_id):
    """Show a single topic and its entries"""
    topic = Topic.objects.get(id=topic_id) # find a topic via its id
    entries = topic.entry_set.order_by('-date-added')
    context = {'topic': topic, 'entries': entries} # return topic and entries as context data
    return render(request, 'build_log/topic.html', context)