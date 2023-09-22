import requests


class HH_VAC:
    def __init__(self, keyword, url):
        self.url = url
        self.params = {
            'text': keyword,
            'page': 0,
            'per_page': 100,
            'search_field': 'name'
        }

    def get_request(self):
        return requests.get(self.url, params=self.params)


class HH_EMP:
    def __init__(self, url):
        self.url = url
        self.params = {

        }

    def get_request(self):
        return requests.get(self.url, params=self.params)
