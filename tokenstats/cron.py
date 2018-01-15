# define cron job which check expiration of feedback post of user
# if That feedback post is expired then just delete that from db also
# python manage.py crontab add to start your job
# python manage.py crontab show to show your job
# python manage.py crontab remove

import requests
import json
# import django
import logging
# import os,sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# #
# sys.path.append('/usr/local/bin/python')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'tokenstats.settings'
# django.setup()
# from django.conf import settings

import cfscrape

from bs4 import BeautifulSoup

from graph.models import TokenData

BASE_URL = "https://min-api.cryptocompare.com/data/"
FSYM = "SNT"
TSYM = "USD"


def _insert_into_db(price, per_hold, total):
    TokenData.objects.create(price=float(price), percentage_holds=float(per_hold.replace("%", '')),
                             total_token=int(total))


def get_snt_price():
    url = BASE_URL + "pricemultifull?fsyms={}&tsyms={}".format(FSYM, TSYM)
    content = requests.get(url)
    if content.status_code == 200:
        data = json.loads(content.text)['RAW'][FSYM][TSYM]
        return data['PRICE']


def get_token_details():
    """
    tuple of two elements
    1: percentage of token hold by top 100 user
    2: total token holders
    :return:
    """
    url = "https://etherscan.io/token/tokenholderchart/0x744d70fdbe2ba4cf95131626614a1763df805b9e"
    scraper = cfscrape.create_scraper()
    page = scraper.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    data = (soup.find("center").get_text()).replace("The Top 100 holders collectively own ", "").split(" ")
    return data[1], data[-1]


def update_token_data():
    try:
        price = get_snt_price()
        per_hold, total_token = get_token_details()
        _insert_into_db(price, per_hold, total_token)
    except Exception as e:
        logging.error(e)
