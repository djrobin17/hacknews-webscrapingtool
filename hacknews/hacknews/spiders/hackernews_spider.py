import scrapy
from ..items import HackernewsItem
from scrapy.utils.response import open_in_browser
class HackerNewsSpider(scrapy.Spider):
    name = 'hackernews'
    start_urls = [
        'https://thehackernews.com/'
    ]

    def parse(self,response):

        open_in_browser(response)

        items = HackernewsItem()

        all_news = response.css('#Blog1 .cf')

        i=0

        for news in all_news:
            headline = news.css('.home-title::text').extract_first()
            date = news.css('.item-label::text').extract_first()
            author = news.css('span::text').extract_first().rstrip("\n")
            link = news.xpath('//a[@class="story-link"]/@href')[i].extract()
            i+=1
            items['headline'] = headline
            items['date'] = date
            items['author'] = author
            items['link'] = link

            yield items

        # next_page = response.css('#Blog1_blog-pager-older-link').xpath('//a[@class="blog-pager-older-link-mobile"]/@href').get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)