import scrapy
import datetime
from textblob import TextBlob

from newscrawler.items import BlogItem, AvgItem

class BingSpider(scrapy.Spider):
    name = "bingspider"

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'} 
        #url = 'https://www.bing.com/news/search?q=realestate&qs=n'
        #request = scrapy.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'})
        urls = [
            'https://www.bing.com/news/search?q=realestate&qs=n&mkt=en-US',
            # 'https://www.bing.com/news/search?q=commercial+realestate&qs=n&mkt=en-US',
            # 'https://www.bing.com/news/search?q=multifamily+realestate&qs=n&mkt=en-US',
            # 'https://www.bing.com/news/search?q=us+realestate&qs=n&mkt=en-US',
            # 'https://www.bing.com/news/search?q=mortgage+market&qs=n&mkt=en-US',
            # 'https://www.bing.com/news/search?q=realestate+market&qs=n&mkt=en-US',
            # 'https://www.bing.com/news/search?q=realestate+investment&qs=n&mkt=en-US',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        cards = response.css("div.news-card-body")
        sentiment_add = 0


        for card in cards:
            item = BlogItem()
            item['title'] = card.css("a.title::text").extract()
            item['snippet'] = card.css('div.snippet::text').extract()
            item['link'] = card.css('a::attr(href)').extract_first()  
            item['date'] = datetime.datetime.today()
            sentiment_test = str(card.css("a.title::text").extract()) + str(card.css('div.snippet::text').extract())
            blob = TextBlob(sentiment_test)
            item['sentiment'] = blob.sentiment.polarity
            sentiment_add += blob.sentiment.polarity
            yield item
        else:
            avg = AvgItem()
            avg['sentiment_avg'] = sentiment_add
            avg['date'] = datetime.datetime.today()
            yield avg
            
        

        
        
        
    def parse_details(self, response):
        pass
        