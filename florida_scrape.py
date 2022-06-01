# Scrapper found at https://hackernoon.com/how-to-scrape-google-with-python-bo7d2tal
# Scope - Program will scrape google search results for "Flordia Man + Month Day" where
# Month and Day are inputted by a function florida_results(month, day)

import requests
import random
from bs4 import BeautifulSoup

def florida_results(month, day):

    query = "Florida man " + str(month) + ' ' + str(day)
    # Replace spaces with + to place into URL
    query = query.replace(' ', '+')
    url = f"https://google.com/search?q={query}"

    # Create user agent for web scrapping
    A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        )
    
    # Create agent for scrapper
    Agent = A[random.randrange(len(A))]
    
    headers = {'user-agent': Agent}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    results = []
    for g in soup.find_all('div', class_='g'):
        # anchor div
        rc = g.find('div', class_='rc')
        # description div
        if rc:
            divs = rc.find_all('div', recursive=False)
            if len(divs) >= 2: # If there enough information to srape
                headline_url = []
                anchor = divs[0].find('a')
                link = anchor['href']   # Link

                # Remove florida man horoscope from similar webistes
                websites_avoid = ['thefloridamantimes.com', 'myfloridamanstory.com', 
                'floridamanbirthdaychallenge.com', 'facebook.com', 'reddit.com', 'wikipedia.org', 
                'www.ilona-andrews.com', 'eventful.com', 'floridaman.totemtattoo.com', 'twitter.com',
                'justice.gov', 'xbtj.naturopatafacile.it', 'tumblr.com', 'arstechnica.com', 'incendar.com']

                test = []
                for i in range(len(websites_avoid)):
                    if websites_avoid[i] in link:
                        test.append('False')
                if 'False' in test:
                    continue
                
                # Capture title
                title = anchor.find('h3').text  # Headline
                if 'florida man' not in title.lower(): # If florida man not in the title
                    continue

                if 'challenge' in title.lower(): # If website referencing Florida Birthday Challenge in website, skip
                    continue

                if 'birthday' in title.lower(): 
                    continue

                if 'top' in title.lower():
                    continue

                title = title.replace('.', '') # Remove '...' for cutoff titles
                # print('DEBUG - Before: ' + str(title))

                # Remove identifer in headline (Can be -, |, or just written after headline)

                if '-' in title:
                    location = title.find('-')
                elif '|' in title:
                    location = title.find('|')

                    if title[location - 1].isspace():
                        if title[location + 1].isspace():
                            title = title[:location]

                if 'Fox News' in title: # Identifier for website, no dash or pipe
                    location = title.find('Fox')
                    if title[location -1].isspace():
                        title = title[:location]
                        # print(title)

                split_link = link.split('/')
                clean_words = []    
                for i in range(len(split_link)):    # Check if url contains longer headline
                    if  len(split_link[i]) > len(title):
                        headline_url = split_link[i]

                        # Clean possible headline and current headline for extra puncuation
                        headline = title
                        headline_url = headline_url.replace('-', ' ')

                        # Clean headline url to remove extra html tags
                        check_headline = headline_url.split(' ')

                        for j in range(len(check_headline)):
                            if 'html' not in check_headline[j]: # Check if no html link with headline
                                if len(check_headline[j]) > 5: # If word longer than 5 letters
                                    if check_headline[j].isalpha():  # Check if only letters
                                        clean_words.append(check_headline[j])
                                else:
                                    clean_words.append(check_headline[j])

                        headline_url = ' '.join(clean_words)
                        # print('DEBUG: Clean:' + str(headline_url))
                        clean_words = []

                        # If headline URL longer than captured title, replace existing title
                        if len(headline_url) > len(headline):
                            # print('DEBUG - Original: ' + title)
                            # print('DEBUG - New: ' + headline_url + '\n')
                            title = headline_url
                            title = title.capitalize()
                # print('DEBUG - After: ' + str(title))

                item = {
                    "datecode": (str(month) + str(day)),
                    "title": title,
                    "link": link
                }
                results.append(item)
    return results