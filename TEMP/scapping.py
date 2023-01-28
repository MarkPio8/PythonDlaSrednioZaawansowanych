import scrapy
import csv
from scrapy.http import HtmlResponse

class CompanySpider(scrapy.Spider):
    name = "companies"
    start_urls = [
        'https://www.food.be/companies/search',
    ]

    def parse(self, response):
        companies = response.xpath("//a[@class='title']/text()").getall()
        with open(r'C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP\companies.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Company Name"])
            for company in companies:
                writer.writerow([company])
