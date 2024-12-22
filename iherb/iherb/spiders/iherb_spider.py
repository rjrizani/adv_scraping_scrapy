import scrapy
from scrapy.http import Response


class IherbSpiderSpider(scrapy.Spider):
    name = "iherb_spider"
    allowed_domains = ["sg.iherb.com"]
    start_urls = ["https://sg.iherb.com/pr/california-gold-nutrition-gold-c-usp-grade-vitamin-c-1-000-mg-60-veggie-capsules/61864"]

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }


    def parse(self, response: Response):
        title = response.css("h1#name ::text")
        print(title)
