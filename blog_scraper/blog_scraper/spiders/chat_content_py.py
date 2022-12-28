import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from blog_scraper.items import BlogScraperItem




class ChatContentPySpider(CrawlSpider):
    name = 'chat_content.py'
    allowed_domains = ['jamiiforums.com']
    start_urls = ['https://www.jamiiforums.com/search/19611298/?q=usafiri&o=relevance']


    rules = [
        Rule
        ]

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 5,
        'FEED_URI': 'blog_scraper.csv',
        'FEED_FORMAT': 'csv'
    }


    def parse(self, response):
        blog = BlogScraperItem()

        blog['title'] = #response.css('span.title::text').get()
        blog['date'] = #response.css('span.date::text').get()
        blog['user'] = #response.css('a.username::text').get()
        blog['content'] = #response.css('div.bbWrapper::text').getall()

        return blog
    
