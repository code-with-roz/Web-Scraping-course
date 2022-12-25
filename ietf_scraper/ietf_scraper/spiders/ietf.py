import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['jamiiforums.com']
    start_urls = ['https://www.jamiiforums.com/threads/usafiri-mtandaoni.2047350/']

    def parse(self, response):
        #title = response.css('span.title::text').get()
        #title = response.xpath('//title/text()').get()
        content = response.xpath('//div[@class="bbWrapper"]/text()').getall()
        
        
        #title = response.xpath()
        return {"title": content}
