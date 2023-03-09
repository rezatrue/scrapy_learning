import scrapy


class FakeplantsSpider(scrapy.Spider):
    name = "fakeplants"
    allowed_domains = ["fake-plants.co.uk"]
    start_urls = ["http://fake-plants.co.uk/"]

    def parse(self, response):
        categories = response.css('.product-category a::attr(href)')
        for category in categories:
            yield response.follow(category.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        products = response.css('li.product_tag-home')
        for product in products:
            item = {
                'cat' : product.css('span.ast-woo-product-category::text').get().strip(),
                'name' : product.css('h2.woocommerce-loop-product__title::text').get().strip(),
                'link' : product.css('a::attr(href)').get(),
            }
            yield item

        #next_page = response.css('a.next.page-numbers').attrib['href']
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_categories)
        pass
