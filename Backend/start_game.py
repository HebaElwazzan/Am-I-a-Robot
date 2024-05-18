import random
import requests
from bs4 import BeautifulSoup
import random
from generate_wiki import Wiki
from generate_gemini import Gemini

class Game:
    def __init__(self):
        """
        correct_guess: either 'wiki' or 'ai'
        """
        self.correct_guess = None
        self.topic = None
        self.glossary = "Glossary_of_artificial_intelligence"
        self.url = None 
        self.paragraph = None

    def get_random_option(self):
        self.correct_guess = random.choice(['wiki', 'ai'])
        return self.correct_guess
    
    def get_wiki_title(self):
        self.topic, self.url = scrapeWikiArticle("https://en.wikipedia.org/wiki/" + self.glossary)


    def get_paragraph(self):
        if self.correct_guess == 'wiki':
            w = Wiki()
            self.paragraph = w.get_wiki_abstract(self.url)
        elif self.correct_guess == 'ai':
            g = Gemini()
            self.paragraph = g.get_gemini_abstract(self.topic)

    def get_result(self, guess):
        if guess == self.correct_guess:
            return True
        return False
        




def scrapeWikiArticle(url):
    """
    Code credit goes to: https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/ 
    Modified a bit by me
    """
    response = requests.get(
		url=url,
	)
	
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")

    allLinks = soup.find(id="bodyContent").find_all("dt", class_="glossary")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        link = link.find("a")
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1: 
            continue

        # Use this link to scrape
        linkToScrape = link
        break
    url = "https://en.wikipedia.org" + linkToScrape['href']
    response = requests.get(
		url=url,
	)
	
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")

    return title.text, "https://en.wikipedia.org" + linkToScrape['href'] #linkToScrape['href'][6:]
            




