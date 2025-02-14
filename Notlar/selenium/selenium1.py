## pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class SeleniumBot:
    def __init__(self,adres="",username="",password="",*args,**kwargs):
        self.username = username
        self.password = password
        self.adres = adres
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,10)

    def visit(self,adres):
        self.driver.get(adres)
        time.sleep(2)


if __name__ == "__main__":
    bot = SeleniumBot()
    bot.visit("https://www.google.com")