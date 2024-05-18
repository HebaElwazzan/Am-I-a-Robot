import unittest
from start_game import Game, scrapeWikiArticle
from generate_wiki import Wiki

class Tests(unittest.TestCase):
    def test_generate_random_option(self):
        g = Game()
        option = g.get_random_option()
        assert option == 'wiki' or option == 'ai'
    
    def test_scrapeWikiArticle(self):
        title, link = scrapeWikiArticle("https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence")
        print(title)
        print(link)

    def test_get_abstract(self):
        w = Wiki()
        title, link = scrapeWikiArticle("https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence")
        abstract = w.get_wiki_abstract(link)
        print(abstract)
        