
import requests
from bs4 import BeautifulSoup
import re 

class Wiki:
    def __init__(self):
        self.abstract = None

    def get_wiki_abstract(self, url):

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        p = soup.find("p")
        abstract = re.sub("\[[^\]]*\]", "", p.text)
        return abstract




