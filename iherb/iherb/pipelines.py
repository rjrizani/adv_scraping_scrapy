# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class IherbPipeline:
    def process_item(self, item, spider):
        item['title'] = item['title'].strip()
        item['price'] = float(item['price'].strip().replace("S$", "").replace("SG$", ""))
        item['product_description'] = self.parsing_whitespaces(item['product_description'])
        item['product_overview'] = self.parsing_whitespaces(item['product_overview'])
        item['rating'] = float(item['rating'].strip())
        item['total_rating'] = int(item['total_rating'].replace(",", ""))
        item['in_stock'] = self.check_stock(item['in_stock'].strip())
        item['data_scraped'] = item['data_scraped'].strip()
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