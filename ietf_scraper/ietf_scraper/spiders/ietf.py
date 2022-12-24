import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['jamiiforums.com']
    start_urls = ['http://jamiiforums.com/']

    def parse(self, response):
        #title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        
        
        #title = response.xpath()
        return {"title": title}
