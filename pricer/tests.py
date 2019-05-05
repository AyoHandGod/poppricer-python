from django.test import TestCase
from pricer.web.web import ppgWebQuery
from pricer.models import Pop


# Create your tests here.
class PricerAppTests(TestCase):

    def test_query(self):
        character = input("Please enter character name: ")
        pops = ppgWebQuery(character)
        print(pops[0].name)