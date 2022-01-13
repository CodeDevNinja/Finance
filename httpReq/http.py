import requests


class Http:
    def __init__(self, base_url=None, header={}) -> None:
        default_header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        }
        self.BASE_URL = base_url
        default_header.update(header)
        self.HEADER = default_header

    def get(self, url, header=None, cookie=None):
        url = self.BASE_URL if not url else url
        header = self.HEADER if not header else header
        return requests.get(url, headers=header,cookies=cookie)
