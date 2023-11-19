import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://example.com/articles']

    def parse(self, response):
        # Extract article titles (assuming they are in <h2> tags)
        titles = response.css('h2::text').extract()
        
        # Print the titles
        for title in titles:
            print(title)
