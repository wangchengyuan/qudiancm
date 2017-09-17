from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import unittest
from data import urldata
from data import logindata

class checOrderOverdue(unittest.TestCase):
    def setUp(self):
        path = '/Library/Frameworks/Python.framework/Versions/3.6/'
        self.driver = webdriver.Chrome(path + 'chromedriver')
        smsc = urldata.smsc
        url = urldata.url
        self.driver.get(url)
        try:
            self.driver.add_cookie(smsc)
        except WebDriverException as e:
            print(e)
            print("添加cookie本身存在的异常")
        self.driver.refresh()
        self.driver.find_element(By.ID, "username").send_keys(logindata.username)
        self.driver.find_element(By.ID, "password").send_keys(logindata.password)
        self.driver.find_element(By.CLASS_NAME, "login").click()

    def tearDown(self):
        self.driver.quit()