import scrapy
from scrapy.loader import ItemLoader
from DemoDownloader.items import DemoDownloaderItem
# This top line is from the items script that comes when starting a new scrapy project
class MPThreeDownloader(scrapy.Spider):
    #The name of the spider when you ask to crawl
    name = 'downloader'
    #Start url of where to scrape
    start_urls = [
        "http://195.122.253.112/public/mp3/Metallica/Albums/1996%20-%20Load/"
    ]
    
    def parse(self, response):
        #This extracts all @href that don't have jpg
        for link in response.xpath("//following::tr[4]/td[2]/a[not(contains(@href, 'jpg'))]"):
            loader = ItemLoader(item=DemoDownloaderItem(), selector=link)
            relative_url = link.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            yield loader.load_item()
