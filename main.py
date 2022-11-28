from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import dotenv_values
from MarketAlert import MarketAlertUM_API
from AmazonScraper import AmazonScraper

# Car = 1
# Boat = 2
# PropertyForRent = 3
# PropertyForSale = 4
# Toys = 5
# Electronics = 6

if __name__ == "__main__":
    config = dotenv_values("./.env")
    marketalertum = MarketAlertUM_API(config['MARKETALERTUM_ID'])
    scraper = AmazonScraper()
    items = scraper.search("ssd")
    for item in items:
        print(item)
        marketalertum.create_alert(item, 6)