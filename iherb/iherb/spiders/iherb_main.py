import scrapy
from ..items import IherbItem
import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IherbMainSpider(CrawlSpider):
    name = "iherb_main"
    allowed_domains = ["sg.iherb.com"]
    start_urls = ["https://sg.iherb.com/new-products"]
    

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    rules = [
        Rule(link_extractor=LinkExtractor(allow=r"p="), follow=True),
        Rule(
            link_extractor=LinkExtractor(allow=r"/pr/"),
            callback="parse_item",
            follow=True,
            process_request="enable_impersonate",
        ),
    ]

    def enable_impersonate(self, request, response):
        request.meta["impersonate"] = "chrome110"
        return request

    def start_requests(self):
        for url in self.start_urls:
            for browser in ["chrome110", "edge99", "safari15_5"]:
                self.logger.info(f"Requesting {url} with browser: {browser}")
                yield scrapy.Request(
                    url,
                    dont_filter=True,
                    meta={"impersonate": browser},
                )

    def parse_item(self, response):
        item = IherbItem()
        
        item['title'] = response.css("h1#name ::text").get()
        item['price'] = response.css("b.s24 ::text").get()

        #item['product_description'] = response.css("ul#product-specs-list li::text").getall() 
        #item['product_overview'] = response.css("div.inner-content ::text").getall() 
        item['manufacturer'] = response.css("div#brand span bdi::text").get()  
        item['manufacturer_website'] = response.css("section.product-overview-link a::attr(href)").get()   
        item['rating'] = response.css("a.average-rating::text").get()
        item['total_rating'] = response.css("a.rating-count span::text").get()
        item['in_stock'] = response.css("strong.text-primary ::text").get()
        #url = response.url
        item['img_url'] = response.css("img#iherb-product-image ::attr(src)").get()  
        item['data_scraped'] = datetime.datetime.now().strftime("%d %B %Y")

        # Include URL for debugging or tracking
        item['url'] = response.url

        self.logger.info(f"Scraped item: {item}")
        yield item

