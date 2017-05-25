import scrapy

from onepiece_wikia.helper.url_retriever import UrlRetriever


class DevilFruitsSpider(scrapy.Spider):
    name = 'devil_fruits'

    def start_requests(self):
        urls = UrlRetriever.retrieve_devil_fruit_urls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = {}
        title = response.xpath(
            '//div[contains(@class,"header-title")]/h1/text()'
        ).extract_first()
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
