from django.shortcuts import render
from .models import Topic, Entry


# Create your views here.
def index(request):
    """The homepage for the build log"""
    return render(request, 'build_log/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')  # add topics into list ordered by date
    context = {'topics': topics}   # set the context name for this list to be accessed in html
    return render(request, 'build_log/topics.html', context) # pass back template and context


def topic(request, topic_title):
    """Show a single topic and its entries"""
    coverage = Topic.objects.get(title=topic_title)  # find a topic via its title
    entries = coverage.entry_set.order_by('-date_added')
    context = {'topic': coverage, 'entries': entries}  # return topic and entries as context data
    return render(request, 'build_log/topic.html', context)


def entry(request, entry_name):
    """Shows a single entry"""
    story = Entry.objects.get(name=entry_name)  # grab the entry via its title
    context = {'entry': story}
    return render(request, 'build_log/entry.html', context)

