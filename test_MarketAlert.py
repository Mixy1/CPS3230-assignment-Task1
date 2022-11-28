import unittest

from MarketAlert import MarketAlertUM_API
from dotenv import dotenv_values

class test_MarketAlert(unittest.TestCase):
    def setUp(self):
        config = dotenv_values("./.env")
        self.marketalert = MarketAlertUM_API(config['MARKETALERTUM_ID'])
        self.marketalert.delete_alert()

    def test_delete_alert(self):
        self.marketalert.delete_alert()
        self.assertEqual(self.marketalert.get_alerts().json(), [])

    def test_create_alert(self):
        self.marketalert.create_alert(
            {
                "title": "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming",
                "price": 1999,
                "image": "https://m.media-amazon.com/images/I/51c0t4J1NWL._AC_UY218_.jpg",
                "description": "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming",
                "url": "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+books&qid=1606856566&sr=8-1"
            },
            6
        )
        items = self.marketalert.get_alerts().json()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['heading'], "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming")
        self.assertEqual(items[0]['priceInCents'], 1999)
        self.assertEqual(items[0]['imageURL'], "https://m.media-amazon.com/images/I/51c0t4J1NWL._AC_UY218_.jpg")
        self.assertEqual(items[0]['description'], "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming")
        self.assertEqual(items[0]['url'], "https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593279280/ref=sr_1_1?dchild=1&keywords=python+books&qid=1606856566&sr=8-1")
        self.assertEqual(items[0]['alertType'], 6)


if __name__ == '__main__':
    unittest.main()
