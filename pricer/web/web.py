import requests
from bs4 import BeautifulSoup
from pricer.models import Pop


BASE_URL = "https://www.poppriceguide.com/guide/searchresults.php?search="


def ppgWebQuery(charactername):
    """
    Searches ppg for supplied charactername
    :param charactername: String value of character name
    :return: list of Pop objects for character
    """
    response = requests.get(BASE_URL + charactername)
    soup = BeautifulSoup(response.content, 'html.parser')
    item_divs = soup.findAll("div", class_= "itemrow")
    pops = []
    for i in range(len(item_divs)):
        name = item_divs[i].findNext("div", class_ = "itemname").string.strip()
        value = item_divs[i].findNext("div", class_="itemvalue").string.strip()
        url = item_divs[i].a['href']
        image_url = item_divs[i].img['src']
        pop = Pop(name=name, value=value, url=url, imageUrl=image_url)
        pops.append(pop)

    return pops

