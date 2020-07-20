# This program uses the scrape Python script to show an example of the results
# This script is an example of how to use the scrape_results library. 

import scrape_results

# define an example website url
website_url = "https://auto.hindustantimes.com/"

# define example keywords
keywords = ["blues", "incentives"]

# Call the scrape functions and get the sentences containing these keywords

scrape_results.scrape(website_url, keywords)