from django.db import models
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.poppriceguide.com/guide/searchresults.php?search="

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)


    def pop_query(self):
        response = requests.get(BASE_URL + self.name)
        soup = BeautifulSoup(response.content, 'html.parser')
        item_divs = soup.findAll("div", {"class": "itemrow"})
        name = item_divs[0].findNext("div", class_ = "itemname").string.strip()
        value = item_divs[0].findNext("div", class_="itemvalue").string.strip()
        url = item_divs[0].a['href']
        image_url = item_divs[0].img['src']

