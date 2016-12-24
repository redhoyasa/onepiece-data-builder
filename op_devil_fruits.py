import scrapy
from url_retriever import UrlRetriever


class OpDevilFruitsSpider(scrapy.Spider):
    name = 'op-devil-fruits'
    start_urls = UrlRetriever.retrieve_devil_fruit_urls()

    def parse(self, response):
        data = {}
        header_title = response.css('.header-title')[0]
        title = header_title.css('h1::text').extract_first()
        data['devilfruit_name'] = title
        data['devilfruit_wiki_url'] = response.url
        data['devilfruit_type'] = 'UNKNOWN'
        data['devilfruit_previous_user'] = None
        data['devilfruit_current_user'] = None

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
