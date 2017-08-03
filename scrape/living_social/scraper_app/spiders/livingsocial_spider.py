#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website livingsocial.com and
save to a database (postgres).

Scrapy spider part - it actually performs scraping.
"""

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(BaseSpider):
    """
    Spider for regularly updated livingsocial.com site, San Francisco page
    """
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["https://www.livingsocial.com/local/san-francisco"]

    deals_list_xpath = '//figure[@class="card-ui cui-c-udc cui-c-udc-featured-list"]'
    item_fields = {
        'title': './/a//div[@class="cui-udc-title c-txt-black two-line-ellipsis"]/text()',
        'link': './/a/@href',
        'location': './/span[@class="cui-location-name "]//text()',
        'original_price': './/s/text()',
        'price': './/div[@class="cui-price"]/span/text()',
        'distance': './/span[@class="cui-location-distance "]//text()'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url https://www.livingsocial.com/local/san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = Selector(response)

        # iterate over deals
        for deal in selector.xpath(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
