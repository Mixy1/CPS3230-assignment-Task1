class mock_search_results_page():
    def __init__(self, results):
        self.results = results
    def get_search_results(self):
        return self.results
    def get_item_page_object(self, result):
        return mock_item_page(result)

class mock_item_page():
    def __init__(self, result):
        self.result = result
    def get_item(self):
        return self.result
    def close(self):
        pass

def mock_landing_page(results):

    class mock_page():
        results = None
        def __init__(self):
            pass
        def search(self, keyword):
            return mock_search_results_page(self.results)
        def close(self):
            pass

    mock_page.results = results
    return mock_page
