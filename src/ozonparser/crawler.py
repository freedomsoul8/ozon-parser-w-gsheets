from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from src.ozonparser.entities import product_service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class CrawlerService:

    def parse(self,url):

        driver.get(url)
        product_service.product.name = driver.find_element(by=By.XPATH,value=product_service.path.name).text
        product_service.product.link = url
        product_service.product.price_ozon_card = driver.find_element(by=By.XPATH,value=product_service.path.ozon_card).text
        product_service.product.price_no_ozon_card = driver.find_element(by=By.XPATH,value=product_service.path.no_ozon_card).text
        product_service.product.price_crossed = driver.find_element(by=By.XPATH,value=product_service.path.crossed).text
        data = (product_service.product.link,
                product_service.product.name,
                product_service.product.price_ozon_card.replace(u"\u2009","").replace("₽",""),
                product_service.product.price_no_ozon_card.replace(u"\u2009","").replace("₽",""),
                product_service.product.price_crossed.replace(u"\u2009","").replace("₽",""))

        return data

crawler = CrawlerService()

# print(crawler.parse("https://www.ozon.ru/product/brelok-dlya-klyuchey-avtomobilya-mazda-mazda-kozhanyy-978584396/?from_sku=978582914&oos_search=false&sh=cIjY6g5XCQ"))



