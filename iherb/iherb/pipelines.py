# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class IherbPipeline:
    def process_item(self, item, spider):
        item = dict(item)  # convert Scrapy.Item to dict
        item['title'] = item['title'].strip() if isinstance(item['title'], str) else item['title']
        item['price'] = float(item['price'].strip().replace("S$", "").replace("SG$", "")) if isinstance(item['price'], str) else item['price']
        #item['product_description'] = self.parsing_whitespaces(item['product_description']) if isinstance(item['product_description'], str) else item['product_description']
        #item['product_overview'] = self.parsing_whitespaces(item['product_overview']) if isinstance(item['product_overview'], str) else item['product_overview']
        item['rating'] = float(item['rating'].strip()) if item['rating'] is not None and isinstance(item['rating'], str) else item['rating']
        item['total_rating'] = int(item['total_rating'].replace(",", "")) if item['total_rating'] is not None and isinstance(item['total_rating'], str) else item['total_rating']
        item['in_stock'] = self.check_stock(item['in_stock'].strip()) if item['in_stock'] is not None and isinstance(item['in_stock'], str) else item['in_stock']
        item['data_scraped'] = item['data_scraped'].strip() if isinstance(item['data_scraped'], str) else item['data_scraped']
        return item

    def parsing_whitespaces(self, value: list[str]) -> list[str]:
        output =  [i.strip() for i in value if len(i.strip()) > 0]
        return output[0]

    def check_stock(self, value: str) -> bool:
        value = value.strip()
        match value:
            case "In stock":
                return True
            case _:
                return False