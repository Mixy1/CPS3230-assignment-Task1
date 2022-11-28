import requests

class MarketAlertUM_API:
    def __init__(self, user_id):
        self.user_id = user_id
        self.base_url = "https://api.marketalertum.com/"

    def create_alert(self, item, alert_type):
        requests.post(self.base_url + "Alert", json={
            "postedBy": self.user_id,
            "heading": item["title"],
            "priceInCents": item["price"],
            "imageUrl": item["image"],
            "description": item["description"],
            "url": item["url"],
            "alertType": alert_type
        })

    def delete_alert(self):
        requests.delete(self.base_url + "Alert/?userId=" + self.user_id)

    def get_alerts(self) -> requests.Response:
        return requests.get(self.base_url + "Alert/?userId=" + self.user_id)
