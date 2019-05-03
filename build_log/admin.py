from django.contrib import admin

from build_log.models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)

