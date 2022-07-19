"""
Scripts for scraping reviews from links.json file
Collect:
-> all reviews with author and score
"""

import requests
from bs4 import BeautifulSoup as bs
import json
import re
import mysql.connector
import config
import datefinder


LINKS_PATH = './src/links.json'
AVAILABLE_MODELS = ["kindle_ads", "kindle_no_ads", 
                    "kindle_paperwhite_ads", "kindle_paperwhite_no_ads",
                    "kindle_paperwhite_signature_edition",  
]
HEADERS = {
    'authority': 'www.amazon.com',
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "dnt": "1",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB;q=0.6',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
}

conf = {
    'host': config.SQL_HOST,
    'user': config.SQL_USER,
    'password': config.SQL_PWD,
    'auth_plugin': config.SQL_AUTH,
    #'db': config.SQL_DB
    }


def read_json(file_path):
    with open(file_path) as json_file:
        amazon_links = json.load(json_file)
    return amazon_links


def get_page_text(website):
    respns = requests.get(website, headers=HEADERS)
    return respns.text


def get_reviews(page):
    soup = bs(page, "lxml")
    reviews = soup.find_all("div", {"class": "a-section celwidget"})
    return reviews


def get_review_text(review):
    return review.find("span", {"class" : "a-size-base review-text review-text-content"}).get_text()


def get_review_id(review):
    return re.search( r'id="customer_review-(.*?)">' ,str(review)).group(1)


def get_review_score(review):
    review.find("span", {"class" : "a-icon-alt"}).get_text()[:1]
    
def get_review_date(review):
    review_date_place = review.find("span", {"class": "review-date"}).get_text()
    review_date = datefinder.find_dates(review_date_place)
    review_date = next(review_date).strftime("%d-%m-%Y")
    return review_date

def get_review_country(review):
    review_date_place = review.find("span", {"class": "review-date"}).get_text()
    return re.search( r'in (.*?) on' ,str(review_date_place)).group(1)


def get_review_elements(review):
    review_id = get_review_id(review)
    review_score = get_review_score(review)
    revieww_text = get_review_text(review)
    review_country = get_review_country(review)
    review_date = get_review_date(review)


def add_review_to_db(review):
    pass

def main():
    df = mysql.connector.connect(**conf
    )
    json_links = read_json(LINKS_PATH)
    test_website = json_links[AVAILABLE_MODELS[0]]['website']
    test_html = get_page_text(test_website)
    reviews = get_reviews(test_html)
    for review in reviews:
        get_review_elements(review)


    
if __name__=="__main__":
    main()