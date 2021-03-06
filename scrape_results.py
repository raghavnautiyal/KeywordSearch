# This script finds a list of keywords on a given site

import requests
from bs4 import BeautifulSoup
import re
import requests
from lxml.html import fromstring

def scrape(website_urls, keywords):
    
    if isinstance(keywords, list) != True:
        print("Keywords must be a list of different words you want to find in the page")
        return 

    if isinstance(website_urls, list) != True:
        print("Website URLs must be a list of different urls you want search for keywords on")
        return 

    i = 0

    for website_url in website_urls:

        response = requests.get(website_url)

        if response.status_code == 200: 
            print(f"\n{fromstring(response.content).findtext('.//title')}: {website_url}\n")
            print("The page opened successfully\n") 

        else:
            print(f"Error: The site could not be reached, and showed status code {response.status_code}.")

        parser = BeautifulSoup(response.text, 'html.parser')

        for keyword in keywords:
            results = parser.body.find_all(string=re.compile(f'.*{keyword}.*'), recursive=True)

            print(f'Found the word "{keyword}" {len(results)} times\n')

            for content in results:

                words = content.split()
                for index, word in enumerate(words):
                    # If the content contains the search word twice or more this will fire for each occurence
                    if word == keyword:
                        print(f'Whole Sentence: "{content}"')
                        # Check if it's a first word
                        if index != 0:
                            before = words[index-1]
                        # Check if it's a last word
                        if index != len(words)-1:
                            after = words[index+1]
                        print(f'Word before: "{before}"') 
                        print(f'word after: "{after}"\n')
        i += 1

        if i == len(website_urls): return 
