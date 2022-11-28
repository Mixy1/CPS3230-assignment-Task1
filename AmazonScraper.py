from AmazonPageObjects import AmazonLandingPageObject

class AmazonScraper:
    def __init__(self, landing_page_object=AmazonLandingPageObject):
        self.landing_page_object = landing_page_object
        pass

    def search(self, keyword):
        """
        keyword: a string
        returns a list of items found
        """
        search_object = self.landing_page_object()
        search_page = search_object.search(keyword)
        search_results = search_page.get_search_results()[:5]
        items = []
        for item in search_results:
            item_object = search_page.get_item_page_object(item)
            data = item_object.get_item()
            if data:
                items.append(data)
            item_object.close()
        search_object.close()
        return items