# Scrapy_learing:

TEST_01[SCRAPY]: https://www.youtube.com/watch?v=s4jtkzHhLzY 

CREATE VERTUAL ENVIRONMENT IN ANACONDA:

conda -V 
conda update conda
conda create -n envname python=x.x anaconda
/[conda create -n envname
conda install python=3.8]
pip install scrapy / conda install -c conda-forge scrapy

conda activate envname
conda install -n yourenvname package
conda deactivate / conda.bat activate base

CREATE SCRAPY PROJECT:

scrapy startproject booksscraper
cd booksscraper
tree

OPEN SCRAPY SHELL:
scrapy shell
fetch('https://books.toscrape.com/')
response.css('article.product_pod').get() return frist product 
response.css('article.product_pod h3 a::text').get() return the text from that tag
response.css('article.product_pod h3 a::text').getall() return all text from the page

response.css('article.product_pod div.product_price p::text').get()	  replace pound sign
response.css('article.product_pod h3 a').attrib['href'] return link

/
products = response.css('article.product_pod')
products.css('h3 a::text').get() return the text from that tag

OPEN SCRAPY PROJECT IN IDE:

C:\Users\REZA\booksscraper project open in the same location were you write the scrapy create command
open project using IDE > write code

RUN CODE:

activate venv > go to the project folder > 
scrapy crawl books

scrapy crawl books -o books.json write file in json
scrapy crawl books -O books.csv Capital O will overwrite file

...........................................................................

