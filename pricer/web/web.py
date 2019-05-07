import requests
from bs4 import BeautifulSoup
from pricer.models import Pop, Character
from django.core.exceptions import *
import logging

BASE_URL = "https://www.poppriceguide.com/guide/searchresults.php?search="


def setupWebDig(charactername):
    """
    prepare Beautiful soup object using html page
    :param charactername: string of character/property name used to complete search
    :return:  parsed html page
    """
    # Get html page and parse it
    response = requests.get(BASE_URL + charactername)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def ppgWebQuery(charactername):
    """
    Searches parsed html for supplied charactername
   :param charactername: String value of character name
   :param soup: parsed html page
   :return: list of Pop objects for character if found. None if no Pops found.
   """

    soup = setupWebDig(charactername)
    # Gather the count of items found on html page. If 0, return None
    item_count = countOfPopsOnPage(soup)
    if item_count == 0:
        return None

    # Gather up the divs that hold Pop information, and create a Character object
    item_divs = soup.findAll("div", class_="itemrow")
    pops = []
    character = Character(name=charactername)

    # For each of the items, create a Pop object and add it to the pops list
    for i in range(len(item_divs)):
        name = item_divs[i].findNext("div", class_="itemname").string.strip()
        strValue = item_divs[i].findNext("div", class_="itemvalue").string.strip()
        value = strValue[1::]
        url = item_divs[i].a['href']
        image_url = item_divs[i].img['src']
        pop = Pop(name=name, value=value, url=url, imageUrl=image_url, character=character)
        pops.append(pop)

    return pops


def countOfPopsOnPage(soupedHtml):
    """
    Parse a souped copy of the ppg search results page and get the item count
    :param soupedHtml: html page parsed in BeautifulSoup html.parsers
    :return: int count of items found
    """
    # Gather the count of items found on html page. If 0, return None
    item_count = int(soupedHtml.find("div", id="guide_dat").b.string.split(" ")[0])
    return item_count


def addPopListToDB(popList):
    """
    Adds a list of Pops to the Database
    :param popList: A list of Pop objects
    :return:
    """
    characterString = popList[0].character.name
    try:
        character = Character.objects.get(name=characterString)

    except ObjectDoesNotExist:
        Character.objects.create(name=characterString)
        character = Character.objects.get(name=characterString)

    for pop in popList:
        Pop.objects.create(name=pop.name, value=pop.value, url=pop.url, imageUrl=pop.imageUrl, character=character)
        print("Added the following: " + pop.__str__())
