# Online Keyword Search

This Python library scrapes a website, using the Beautifulsoup module, and looks for the keywords you specify. If the keywords are found, it returns the number of times each keyword was found, all the sentences containing each keyword, and the words before, and after each keyword. This can be seamlessly integrated with databases.

# Prerequisites

There are a few prerequisites that are needed for the functioning of this library:

-   Python (Version 3.6 or above): Since this repository was written in Python, it is one of the prime requirements. Download Python at [python.org/downloads/](https://www.python.org/downloads/)

-   BeautifulSoup: BeautifulSoup is a Python package for parsing HTML and XML documents. You can install BeautifulSoup by running <code>pip install bs4</code> in your terminal.

-   Requests: Requests is a Python HTTP library, which makes HTTP requests simpler and more human-friendly. You can install Requests by running <code>pip install requests</code> in your terminal.

-   Regular Expressions: Python has a built-in package called re, which can be used to work with Regular Expressions. A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. You can install re by running <code>pip install re</code> in your terminal.

# Example

You can look at an example of how to use this library in the example.py file. You can call the <code>scrape_results</code> function, and pass in a list of websites and a list of keywords you want to find.
