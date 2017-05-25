import scrapy


class CharactersSpider(scrapy.Spider):
    name = 'characters'

    def start_requests(self):
        urls = ['http://onepiece.wikia.com/wiki/List_of_Canon_Characters']
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
