"""
How it works:
- First a wikipedia scraper script finds a random wikipedia article title
- Then a random fair variable decides whether the content will be AI generated or scraped off wikipedia
- If AI generated, the title previously generated is passed to Gemini within a prompt
- Otherwise the abstract of the wikipedia article is extracted
- The user chooses their guess and gets verified
Additional: some things in wikipedia make it obvious that it is from wikipedia
Either try to find a way to filter those
OR ask gemini to mimic wikipedia's style
"""