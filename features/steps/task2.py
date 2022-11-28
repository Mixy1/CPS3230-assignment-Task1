from behave import *
from MarketAlert import MarketAlertUM_API
from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging

dummy_object = {
    "title": "Samsung 860 EVO 1TB 2.5 Inch SATA III Internal SSD (MZ-76E1T0B/AM)",
    "price": 10999,
    "image": "https://images-na.ssl-images-amazon.com/images/I/71WgXGmdKWL._AC_SL1500_.jpg",
    "description": "Samsung 860 EVO 1TB 2.5 Inch SATA III Internal SSD (MZ-76E1T0B/AM)",
    "url": "https://www.amazon.com/Samsung-2-5-Inch-Internal-MZ-76E1T0B-AM/dp/B0781Z7Y3S/ref=sr_1_1?dchild=1&keywords=ssd&qid=1606856566&sr=8-1"
}


def login(context):
    context.marketalertDriver.get("https://www.marketalertum.com/Alerts/Login")
    context.marketalertDriver.find_element(By.ID, "UserId").send_keys(context.userid + Keys.RETURN)

@given('I am a user of marketalertum')
def step_impl(context):
    assert context.userid is not None

@when('I login using valid credentials')
def step_impl(context):
    login(context)    

@then('I should see my alerts')
def step_impl(context):
    # Assert that page contains "My Alerts"
    assert "Latest alerts for Michael Debono" in context.marketalertDriver.page_source

@when(u'I login using invalid credentials')
def step_impl(context):
    context.marketalertDriver.get("https://www.marketalertum.com/Alerts/Login")
    context.marketalertDriver.find_element(By.ID, "UserId").send_keys("invalid" + Keys.RETURN)

@then(u'I should see the login screen again')
def step_impl(context):
    assert "User ID:" in context.marketalertDriver.page_source

@given(u'I am an administrator of the website and I upload {num:d} alerts')
def step_impls(context, num):
    login(context)
    for _ in range(num):
        context.marketalertApi.create_alert(dummy_object, 6)

@when(u'I view a list of alerts')
def step_impl(context):
    context.marketalertDriver.get("https://www.marketalertum.com/Alerts/List")
    assert "Latest alerts for Michael Debono" in context.marketalertDriver.page_source

@then(u'each alert should contain an icon')
def step_impl(context):
    context.alerts = context.marketalertDriver.find_elements(By.TAG_NAME, "table")
    for alert in context.alerts:
        assert alert.find_element(By.XPATH, "//tbody/tr[1]/td/h4/img") is not None

@then(u'each alert should contain a heading')
def step_impl(context):
    for alert in context.alerts:
        assert alert.find_element(By.TAG_NAME, "h4") is not None

@then(u'each alert should contain a description')
def step_impl(context):
    for alert in context.alerts:
        # check that tr>td>text exists
        assert alert.find_element(By.XPATH, "//tbody/tr[3]/td").text is not None

@then(u'each alert should contain an image')
def step_impl(context):
    for alert in context.alerts:
        assert alert.find_element(By.XPATH, "//tbody/tr[2]/td/img") is not None


@then(u'each alert should contain a price')
def step_impl(context):
    for alert in context.alerts:
        assert alert.find_element(By.XPATH, "//tbody/tr[4]/td").text is not None
        assert alert.find_element(By.XPATH, "//tbody/tr[4]/td").text.startswith("Price: €")

@then(u'each alert should contain a link to the original product website')
def step_impl(context):
    for alert in context.alerts:
        assert alert.find_element(By.XPATH, "//tbody/tr[5]/td/a") is not None

@given(u'I am an administrator of the website and I upload more than {num} alerts')
def step_impl(context, num):
    login(context)
    for _ in range(int(num) + 1):
        context.marketalertApi.create_alert(dummy_object, int(num) + 1)

@given(u'I am an administrator of the website and I upload an alert of type {alert_type}')
def step_impl(context, alert_type):
    login(context)
    context.alert_type = int(alert_type)
    context.marketalertApi.create_alert(dummy_object, int(alert_type))


@then(u'I should see {num} alerts')
def step_impl(context, num):
    context.marketalertDriver.get("https://www.marketalertum.com/Alerts/List")
    assert "Latest alerts for Michael Debono" in context.marketalertDriver.page_source
    context.alerts = context.marketalertDriver.find_elements(By.TAG_NAME, "table")
    assert len(context.alerts) == int(num)

@then(u'the icon displayed should be {icon}')
def step_impl(context, icon):
    img = context.alerts[0].find_element(By.XPATH, "//tbody/tr[1]/td/h4/img").get_attribute("src")
    logging.info(img)
    assert img.endswith(icon)