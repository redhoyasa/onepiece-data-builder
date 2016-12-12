import requests


class UrlRetriever():

    SEARCH_URL = 'http://onepiece.wikia.com/api/v1/Articles/List'
    ROOT_URL = 'http://onepiece.wikia.com'

    @classmethod
    def retrieve_devil_fruit_urls(self):
        devil_fruit_urls = []
        devil_fruit_types = ['Paramecia', 'Zoan', 'Logia']

        for devil_fruit_type in devil_fruit_types:
            url_params = {
                'category': devil_fruit_type,
                'limit': 1000
            }

            r = requests.get(self.SEARCH_URL, params=url_params)

            categories = r.json()['items']

            for category in categories:
                if 'Category:' not in category['url']:
                    devil_fruit_urls.append('{}{}'.format(
                        self.ROOT_URL,
                        category['url']))

        return devil_fruit_urls
