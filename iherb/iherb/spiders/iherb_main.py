import scrapy
from ..items import IherbItem
import datetime


class IherbMainSpider(scrapy.Spider):
    name = "iherb_main"
    allowed_domains = ["sg.iherb.com"]
    start_urls = ["https://sg.iherb.com/pr/walden-farms-chicken-dip-n-sauce-buffalo-bleu-11-5-fl-oz-340-ml/142611"]
    #start_urls = ["https://sg.iherb.com/pr/california-gold-nutrition-gold-c-usp-grade-vitamin-c-1-000-mg-60-veggie-capsules/61864"]

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    def start_requests(self):
        for browser in ["chrome110", "edge99", "safari15_5"]:
            yield scrapy.Request(
                #"https://sg.iherb.com/pr/california-gold-nutrition-gold-c-usp-grade-vitamin-c-1-000-mg-60-veggie-capsules/61864",
                "https://sg.iherb.com/pr/walden-farms-chicken-dip-n-sauce-buffalo-bleu-11-5-fl-oz-340-ml/142611",
                dont_filter=True,
                meta={"impersonate": browser},
            )

    def parse(self, response):
        item = IherbItem()
        
        item['title'] = response.css("h1#name ::text").get()
        item['price'] = response.css("b.s24 ::text").get()

        item['product_description'] = response.css("ul#product-specs-list li::text").getall() 
        item['product_overview'] = response.css("div.inner-content ::text").getall() 
        item['manufacturer'] = response.css("div#brand span bdi::text").get()  
        item['manufacturer_website'] = response.css("section.product-overview-link a::attr(href)").get()   
        item['rating'] = response.css("a.average-rating::text").get()
        item['total_rating'] = response.css("a.rating-count span::text").get()
        item['in_stock'] = response.css("strong.text-primary ::text").get()
        url = response.url
        item['img_url'] = response.css("img#iherb-product-image ::attr(src)").get()  
        item['data_scraped'] = datetime.datetime.now().strftime("%d %B %Y")

        yield item

