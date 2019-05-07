from django.test import TestCase
from pricer.web.web import ppgWebQuery, addPopListToDB
from pricer.models import Pop


# Create your tests here.
class PricerAppTests(TestCase):

    def test_query(self):
        character = input("Please enter character name: ")
        pops = ppgWebQuery(character)
        print(pops[0].name)
        print(pops[0].value)
        print(pops[0].url)
        print(pops[0].imageUrl)


    def test_db_add(self):
        character = input("Please enter character name: ")
        pops = ppgWebQuery(character)
        addPopListToDB(pops)