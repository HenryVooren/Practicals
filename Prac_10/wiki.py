"""
CP1404 Practical 10
wikipedia API test program
Henry Vooren 2021
"""

import wikipedia


def test_wiki_api():
    """
    search term Monty did not return a disambiguation
    """
    user_search = input("Enter search >>> ")
    while user_search != "":
        try:
            search_page = wikipedia.page(user_search)
            print(search_page.title)
            print(search_page.summary)
            print(search_page.url)
        except wikipedia.exceptions.DisambiguationError as search:
            print(search.options)

        user_search = input("Enter search >>> ")


test_wiki_api()
