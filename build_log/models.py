from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.TextField(max_length=65, null=True)
    text = models.TextField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entities'

    def __str__(self):
        return self.text[:50] + '....'

    def entry_topic(self):
        return 'This entry: {} is from the topic: {}'.format(
            self.name, self.topic
        )
