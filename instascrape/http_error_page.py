from __future__ import annotations

from instascrape import static_scraper
from instascrape import json_scraper

class HttpErrorPage(static_scraper.StaticHTMLScraper):
    """
    Representation of an Instagram profile page.

    Attribues
    ---------
    url : str
        Full URL to an existing Instagram profile

    Methods
    -------
    static_load(session=requests.Session())
        Makes request to URL, instantiates BeautifulSoup, finds JSON data,
        then parses JSON data.
    """

    def _scrape_json(self, json_data: dict):
        """Scrape JSON data and load into instances namespace"""
        self.data = HttpErrorPageJSON(json_data)
        self._load_json_into_namespace(self.data)

class HttpErrorPageJSON(json_scraper.JSONScraper):
    def parse_json(self):
        super().parse_json()

if __name__ == "__main__":
    url = r"https://www.instagram.com/idkdidkdidkdidkdkdidkkdidikd"
    http_error_page = HttpErrorPage(url)
    http_error_page.static_load()
