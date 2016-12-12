import scrapy
from url_retriever import UrlRetriever

print UrlRetriever.retrieve_devil_fruit_urls()


class OnePieceWikiaSpider(scrapy.Spider):
    name = 'One Piece'
    # start_urls = UrlRetriever.retrieve_devil_fruit_urls()
    start_urls = ['http://onepiece.wikia.com/wiki/Yami_Yami_no_Mi']

    def parse(self, response):
        print response
