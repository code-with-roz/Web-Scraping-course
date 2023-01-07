import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from blog_scraper.items import BlogScraperItem


class ChatContentPySpider(CrawlSpider):
    name = 'chat_content.py'
    allowed_domains = ['jamiiforums.com']
    start_urls = ['https://www.jamiiforums.com/search/19611298/?q=usafiri&o=relevance']


    rules = [
        Rule(LinkExtractor(allow=r'/threads/'), callback='parse_info', follow=True)
        ]

    # custom_settings = {
    #     'CLOSESPIDER_PAGECOUNT': 5,
    #     'FEED_URI': 'blog_scraper.csv',
    #     'FEED_FORMAT': 'csv'
    # }


    def parse_info(self, response):
        blog = BlogScraperItem()

        # blog['title'] = response.xpath('//h1/text()').get()
        # blog['date'] = response.xpath('//h1/text()').get()
        # blog['user'] = response.xpath('//h1/text()').get()
        # blog['tags'] = response.xpath('//h1/text()').get()
        # blog['reply_count'] = response.xpath('//h1/text()').get()
        # blog['forum'] = response.xpath('//h1/text()').get()
        # blog['content'] = response.xpath('//h1/text()').get()

        blog['content'] = response.xpath('//div[@class="bbWrapper"]/text()').getall()

        return blog
        
    
