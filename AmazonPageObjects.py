from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re

class AmazonItemPageObject:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Edge('./msedgedriver.exe')
        self.driver.get(url)
    
    def get_title(self):
        return self.driver.find_element(By.ID, "productTitle").text

    def get_price(self):
        try:
            price = self.driver.find_element(By.ID, "price").text
        except NoSuchElementException:
            price = self.driver.find_element(By.ID, "corePrice_feature_div").text
        return price

    def get_price_in_cents(self):
        price = self.get_price()
        # replace every character not a digit with nothing
        price = re.sub(r"[^\d]", "", price)
        return int(price)

    def get_image(self):
        try:
            return self.driver.find_element(By.ID, "imgBlkFront").get_attribute("src")
        except NoSuchElementException:
            return self.driver.find_element(By.ID, "landingImage").get_attribute("src")
        

    def get_description(self):
        return self.get_title()

    def get_item(self):
        return {
            "title": self.get_title(),
            "price": self.get_price_in_cents(),
            "image": self.get_image(),
            "description": self.get_description(),
            "url": self.url
        }

    def close(self):
        self.driver.close()

class AmazonLandingPageObject:
    def __init__(self):
        self.driver = webdriver.Edge('./msedgedriver.exe')
        self.driver.get("https://www.amazon.com")
        try:
            self.accept_cookies()
        except NoSuchElementException:
            pass

    def accept_cookies(self):
        accept_cookies_button = self.driver.find_element(By.ID, "sp-cc-accept")
        accept_cookies_button.click()

    def search(self, search_term):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.ENTER)
        return AmazonSearchResultsPageObject(self.driver)

    def close(self):
        self.driver.close()

class AmazonSearchResultsPageObject:
    def __init__(self, driver):
        self.driver = driver

    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

    def get_link_from_item(self, item):
        return item.find_element(By.TAG_NAME, "a").get_attribute("href")

    def get_item_page_object(self, item):
        return AmazonItemPageObject(self.get_link_from_item(item))

    # Doesn't need a close method as it doesn't own the driver.