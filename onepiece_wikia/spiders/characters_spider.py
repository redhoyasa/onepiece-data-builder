import scrapy
from urllib import parse


class CharactersSpider(scrapy.Spider):
    name = 'characters'

    def start_requests(self):
        urls = ['http://onepiece.wikia.com/wiki/List_of_Canon_Characters']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        list_of_character_page = response.xpath(
            '//table[1]/tr')

        base_url = 'http://onepiece.wikia.com'

        for character_page in list_of_character_page:
            page_link = character_page.xpath(
                'td[2]/a/@href').extract_first()

            if page_link:
                next_page = base_url + page_link
                yield scrapy.Request(
                    next_page, callback=self.crawl_character_page)

    def crawl_character_page(self, response):
        data = {}
        data['character_name'] = response.xpath(
            '//div[contains(@class,"header-title")]/h1/text()'
        ).extract_first()
        data['character_name'] = parse.unquote(data['character_name'])

        data['character_wiki_url'] = response.url
        data['character_wiki_url'] = parse.unquote(data['character_wiki_url'])
        data['character_bounty'] = None

        pi_data = response.xpath(
            '//div[contains(concat(" ",@class," ")," pi-data ")]'
        )

        for pi_data_row in pi_data:
            label = pi_data_row.xpath('h3/text()').extract_first()

            if label == 'Bounty:':
                data['character_bounty'] = pi_data_row.xpath(
                    'div/text()'
                ).extract_first()

        yield data
