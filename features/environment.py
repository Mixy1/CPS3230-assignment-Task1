from dotenv import dotenv_values
from selenium import webdriver
from MarketAlert import MarketAlertUM_API

def before_all(context):
    context.userid = dotenv_values("./.env")["MARKETALERTUM_ID"]
    context.marketalertApi = MarketAlertUM_API(dotenv_values("./.env")["MARKETALERTUM_ID"])
    context.marketalertApi.delete_alert()

def before_scenario(context, scenario):
    context.marketalertDriver = webdriver.Edge("./msedgedriver.exe")

def after_scenario(context, scenario):
    context.marketalertApi.delete_alert()
    context.marketalertDriver.close()