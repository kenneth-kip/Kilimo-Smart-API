""" Web Scraper """

from datetime import date, datetime
import requests

from bs4 import BeautifulSoup

from ..util.model_helper import get_or_create
from ..models.region import Region
from ..models.produce import Produce
from ..models.price import Price
from .. import db


class PriceScraper:
    """ Web Scraper """

    def __init__(self, rows):
        self.__rows = rows

    def update_new_prices(self):
        self.__fetch_and_update_regions()
        self.__fetch_and_update_produce_items()
        region_ids = {region.name: region.id for region in Region.query.all()}
        produce_ids = {
            produce.name: produce.id for produce in Produce.query.all()}
        for row in self.__rows:
            price = row
            region = price['location']
            produce = price['produce']
            price.pop('location')
            price.pop('produce')

            price['produce_id'] = produce_ids[produce]
            price['region_id'] = region_ids[region]
            price['low_price'] = float(price['low_price'].replace(',', ''))
            price['high_price'] = float(price['high_price'].replace(',', ''))
            price['date'] = self.__get_date()
            get_or_create(db.session, Price, **price)

    def __fetch_and_update_regions(self):
        """ Fetches and updates regions table """
        regions = list(
            set([row['location'] for row in self.__rows]))
        for region in regions:
            get_or_create(db.session, Region, name=region)

    def __fetch_and_update_produce_items(self):
        """ Fetches and updates produce table """
        produce_items = list(set([row['produce'] for row in self.__rows]))
        for produce in produce_items:
            get_or_create(db.session, Produce, name=produce)

    def __get_date(self):
        """ Gets the date from scraped data"""
        day_information = datetime.now()
        return day_information
