import scrapy
import pandas as pd
from url_retriever import UrlRetriever


class OnePieceWikiaSpider(scrapy.Spider):
    name = 'One Piece'
    start_urls = UrlRetriever.retrieve_devil_fruit_urls()
    # start_urls = ['http://onepiece.wikia.com/wiki/Mera_Mera_no_Mi']

    def parse(self, response):
        data = {}
        header_title = response.css('.header-title')[0]
        title = header_title.css('h1::text').extract_first()
        data['devilfruit_name'] = title

        for pi_data in response.css('.pi-data'):
            label = pi_data.css('.pi-data-label::text').extract_first()

            if label == 'Type:':
                data['devilfruit_type'] = \
                    pi_data.css('div.pi-data-value a::text').extract_first()

            if label == 'Previous User:':
                data['devilfruit_previous_user'] = \
                    pi_data.css('div.pi-data-value a::text').extract_first()

            if label == 'Current User:':
                data['devilfruit_current_user'] = \
                    pi_data.css('div.pi-data-value a::text').extract_first()

        yield data
