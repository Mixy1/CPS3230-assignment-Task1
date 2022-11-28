import unittest
from AmazonPageObjects import *

class TestAmazonLanding(unittest.TestCase):
    def test_search(self):
        search_object = AmazonLandingPageObject()
        search_page = search_object.search("python books")
        self.assertTrue(type(search_page) == AmazonSearchResultsPageObject)
        search_results = search_page.get_search_results()
        self.assertTrue(len(search_results) > 0)
        search_object.close()

class TestAmazonItem(unittest.TestCase):
    def test_item_normal(self):
        item_object = AmazonItemPageObject("https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/")
        item = item_object.get_item()
        self.assertTrue(item["title"] == "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming")
        # Don't test for price as it changes very often
        self.assertTrue(type(item["price"]) == int)
        self.assertTrue(item["image"] == "https://m.media-amazon.com/images/I/51OOCVBfCQL._SX377_BO1,204,203,200_.jpg")
        self.assertTrue(item["description"] == "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming")
        self.assertTrue(item["url"] == "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/")
        item_object.close()

    # This handles the case when the price isn't in the normal format.
    def test_item_different_price(self):
        item_object = AmazonItemPageObject("https://www.amazon.com/Python-Programming-Beginners-Comprehensive-Hands/dp/B0BFV21L24/")
        item = item_object.get_item()
        self.assertTrue(item["title"] == "Python Programming for Beginners: The Most Comprehensive Programming Guide to Become a Python Expert from Scratch in No Time. Includes Hands-On Exercises")
        self.assertTrue(type(item["price"]) == int)
        self.assertTrue(item["image"] == "https://m.media-amazon.com/images/I/51bP6Oss0SL._SX384_BO1,204,203,200_.jpg")
        self.assertTrue(item["description"] == "Python Programming for Beginners: The Most Comprehensive Programming Guide to Become a Python Expert from Scratch in No Time. Includes Hands-On Exercises")
        self.assertTrue(item["url"] == "https://www.amazon.com/Python-Programming-Beginners-Comprehensive-Hands/dp/B0BFV21L24/")
        item_object.close()

    def test_item_not_book(self):
        item_object = AmazonItemPageObject("https://www.amazon.com/SAMSUNG-Internal-Gaming-MZ-V8P2T0B-AM/dp/B08RK2SR23/")
        item = item_object.get_item()
        self.assertTrue(item["title"] == "SAMSUNG 980 PRO SSD 2TB PCIe NVMe Gen 4 Gaming M.2 Internal Solid State Hard Drive Memory Card, Maximum Speed, Thermal Control, MZ-V8P2T0B")
        self.assertTrue(type(item["price"]) == int)
        self.assertTrue(item["image"] == "https://m.media-amazon.com/images/I/81zJ87YqekL._AC_SX679_.jpg")
        self.assertTrue(item["description"] == "SAMSUNG 980 PRO SSD 2TB PCIe NVMe Gen 4 Gaming M.2 Internal Solid State Hard Drive Memory Card, Maximum Speed, Thermal Control, MZ-V8P2T0B")
        self.assertTrue(item["url"] == "https://www.amazon.com/SAMSUNG-Internal-Gaming-MZ-V8P2T0B-AM/dp/B08RK2SR23/")
        item_object.close()

if __name__ == "__main__":
    unittest.main()