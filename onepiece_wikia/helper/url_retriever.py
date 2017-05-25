import requests


class UrlRetriever():

    SEARCH_URL = 'http://onepiece.wikia.com/api/v1/Articles/List'
    ROOT_URL = 'http://onepiece.wikia.com'

    @classmethod
    def retrieve_devil_fruit_urls(self):
        devil_fruit_urls = []
        devil_fruit_types = ['Paramecia', 'Zoan', 'Logia']
        excluded_url = [
            '/wiki/Artificial_Devil_Fruit',
            '/wiki/Paramecia',
            '/wiki/Logia',
            '/wiki/Zoan'
        ]

        for devil_fruit_type in devil_fruit_types:
            url_params = {
                'category': devil_fruit_type,
                'limit': 1000
            }

            r = requests.get(self.SEARCH_URL, params=url_params)

            items = r.json()['items']

            for item in items:
                is_devil_fruit_url = (
                    ('Category:' not in item['url']) and
                    (item['url'] not in excluded_url)
                )

                if is_devil_fruit_url:
                    devil_fruit_urls.append('{}{}'.format(
                        self.ROOT_URL,
                        item['url'])
                    )

        return devil_fruit_urls
