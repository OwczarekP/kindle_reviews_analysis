"""
Scripts for scraping reviews from links.json file
Collect:
-> all reviews with author and score
"""

import requests
from bs4 import BeautifulSoup as bs
import json


LINKS_PATH = './src/links.json'
AVAILABLE_MODELS = ["kindle_ads", "kindle_no_ads", 
                    "kindle_paperwhite_ads", "kindle_paperwhite_no_ads",
                    "kindle_paperwhite_signature_edition",  
]


def read_json(file_path):
    with open(file_path) as json_file:
        amazon_links = json.load(json_file)
    return amazon_links


def main():
    json_links = read_json(LINKS_PATH)
    print(json_links[AVAILABLE_MODELS[0]]['website'])
    
if __name__=="__main__":
    main()