import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for products in response.css('article.product_pod'):
            try:
                yield{
                    'name': products.css('h3 a::text').get(),
                    'price': products.css('div.product_price p::text').get().replace('£', ''),
                    'link': products.css('h3 a').attrib['href'],
                }
            except:
                yield {
                    'name': products.css('h3 a::text').get(),
                    'price': products.css('div.product_price p::text').get().replace('£', ''),
                    'link': products.css('h3 a').attrib['href'],
                }

        next_page = response.css('li.next a').attrib['href']
        full_url = self.start_urls[0] + next_page
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)