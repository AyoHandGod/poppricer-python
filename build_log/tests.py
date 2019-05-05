from django.test import TestCase
from build_log.models import Entry, Topic


# Create your tests here.
class ModelTestCase(TestCase):

    def test_entry(self):
        topic = Topic(title="Applications")
        entry = Entry(name="Ps5", topic=topic)
        print(entry.entry_topic())
        self.assertEqual(entry.entry_topic(),
                         "This entry: Ps5 is from the topic: Applications",
                         "This worked!")