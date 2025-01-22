"""
Make a web scraper that collects all the links or images from a website and puts them into a list
Delete any duplicates which show up
Try to see if you can make a general web scraper that works with most websites.
"""

from bs4 import BeautifulSoup
import requests
import random

def websiteScraper(url):
    """
    Scrape wikipedia starting from given URL. Keep bouncing between URLs.

    Keyword arguments:
    url -- Given URL that is the start of the bouncing.
    """
    # Get the HTML code for the URL
    response = requests.get(url=url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the title
    title = soup.find(id="firstHeading")
    print(title.text)

    # Find all <a> within the bodyContent of the artical
    all_links = soup.find(id="bodyContent").find_all('a')
    random.shuffle(all_links)
    linktoscrape = 0
    for link in all_links:
        # Find <a> with <href> that contains 'wiki'
        if link['href'].find('/wiki/') == -1:
            continue
        linktoscrape = link
        break
    try:
        websiteScraper("https://en.wikipedia.org" + linktoscrape['href'])
    except KeyError:
        raise KeyError("eiuewhiawrh")


def user_input():
    """Allow for users to put in whatever wikipedia artical they want"""
    user_url = input("Please enter a wikipedia url: ")
    websiteScraper(user_url)


if __name__ == "__main__":
    user_input()
