"""
Make a web scraper that collects all the links or images from a website and puts them into a list
Delete any duplicates which show up
Try to see if you can make a general web scraper that works with most websites.
"""

"""
Goals for tomorrow:
Add a helper function to get rid of any duplicate codes
    - I see one or two duplicate pieces of code in this file. See if you can create helper functions to get rid of these.
"""

from bs4 import BeautifulSoup
import requests
import random

def wikipedia_scraper(url, max=10, current=0):
    """
    Scrape wikipedia starting from given URL. Keep bouncing between URLs.

    Keyword arguments:
    url -- Given URL that is the start of the bouncing.
    """

    # Break the loop
    if current >= max:
        return

    # Get the HTML code for the URL
    response = requests.get(url=url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the title
    title = soup.find(id="firstHeading")
    print(f"{title.text}")

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
        current += 1
        wikipedia_scraper("https://en.wikipedia.org" + linktoscrape['href'], max, current)
    except KeyError:
        raise KeyError("eiuewhiawrh")


def lol_scraper(url, max=10, current=0):
    """
    This function will scrape the lol.fandom.com website.

    Keyword arguments:
    url -- Given url that is the start of the scraping
    max -- The max amount of times for recursion
    current -- The current recursion depth we are at
    """

    if current >= max:
        return

    response = requests.get(url=url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    #Find the title
    title = soup.find(id="firstHeading")
    print(title.text)

    all_links = soup.find(id="content").find_all('a')
    random.shuffle(all_links)
    linktoscrape = 0
    
    for link in all_links:
        if link['href'].find('/wiki/') == -1:
            continue
        linktoscrape = link
        break
    try: 
        current += 1
        lol_scraper("https://lol.fandom.com" + linktoscrape['href'], max, current)
    except KeyError:
        raise KeyError("wiaohioh")


def all_link_scraper(url, max=10, current=0):
    """
    Scrape wikipedia starting from given URL. Keep bouncing between URLs.

    Keyword arguments:
    url -- Given URL that is the start of the bouncing.
    """

    # Get the HTML code for the URL
    response = requests.get(url=url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    link_list = []
    # Find all <a> within the bodyContent of the artical
    all_links = soup.find(id="bodyContent").find_all('a')
    for link in all_links:
        # Find <a> with <href> that contains 'wiki'
        try:
            # Such long IF statements man. They're so long I had to split them in 2.
            # This shit is not efficient at all >_<
            # Oh well, This is only a for-fun project anyways.
            if link['href'] not in link_list and link['href'].find('/wiki/') != -1 and link['href'].find('/wiki/Category') == -1 and link['href'].find('/wiki/Help') == -1:
                if link['href'].find('/wiki/Special') == -1 and link['href'].find('/wiki/Template') == -1 and link['href'].find('/wiki/File') == -1:
                    link_list.append(link['href'])
        except KeyError:
            pass
    
    for i in link_list:
        print(i[6:])



def website_print():
    website_list = ["lol.fandom.com", "wikipedia.org", "wikipedia.org but obtain list of every link"]
    for i in range(len(website_list)):
        print(f"{i + 1}, {website_list[i]}")


def user_input():
    """Allow for users to put in whatever wikipedia artical they want"""
    what_scrape = "ab"
    website_print()
    while not isinstance(what_scrape, int):
        try:
            what_scrape = int(input("What website should we scrape? "))
        except ValueError:
            continue
    
    match what_scrape:
        case 1:
            user_url = input("Please enter a lol.fandom.com player/team url: ")
            lol_scraper(user_url)
        case 2:
            user_url = input("Please enter a wikipedia url: ")
            wikipedia_scraper(user_url)
        case 3:
            user_url = input("Please enter a wikipedia url: ")
            all_link_scraper(user_url)


if __name__ == "__main__":
    user_input()
