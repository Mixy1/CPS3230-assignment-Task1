import unittest
from AmazonScraper import AmazonScraper
from mock_AmazonPageObjects import mock_landing_page

class test_AmazonScraper(unittest.TestCase):
    def test_search(self):
        results = [
            {
                "title": "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming",
                "price": 1999,
                "image": "https://m.media-amazon.com/images/I/51c0t4J1NWL._AC_UY218_.jpg",
                "description": "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming",
                "url": "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+books&qid=1606856566&sr=8-1"
            },
            {
                "title": "Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython",
                "price": 3999,
                "image": "https://m.media-amazon.com/images/I/51H0w6zJG6L._AC_UY218_.jpg",
                "description": "Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython",
                "url": "https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=sr_1_2?dchild=1&keywords=python+books&qid=1606856566&sr=8-2"
            },
            {
                "title": "Automate the Boring Stuff with Python: Practical Programming for Total Beginners",
                "price": 1999,
                "image": "https://m.media-amazon.com/images/I/51ZgB4XsCJL._AC_UY218_.jpg",
                "description": "Automate the Boring Stuff with Python: Practical Programming for Total Beginners",

                "url": "https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_3?dchild=1&keywords=python+books&qid=1606856566&sr=8-3"
            }
        ]
        scraper = AmazonScraper(mock_landing_page(results))
        self.assertEqual(scraper.search("python books"), results)

if __name__ == "__main__":
    unittest.main()

