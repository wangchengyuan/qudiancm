from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import unittest
from data import logindata
from data import urldata
class justTest(unittest.TestCase):
    def setUp(self):
        path = '/Library/Frameworks/Python.framework/Versions/3.6/'
        self.driver=webdriver.Chrome(path+'chromedriver')
        smsc = urldata.smsc
        url = urldata.url
        self.driver.get(url)
        try:
            self.driver.add_cookie(smsc)
        except WebDriverException as e:
            print(e)
            print("添加cookie本身存在的异常")
        self.driver.refresh()
        self.driver.find_element(By.ID,"username").send_keys(logindata.username)
        self.driver.find_element(By.ID,"password").send_keys(logindata.password)
        self.driver.find_element(By.CLASS_NAME, "login").click()


    def tearDown(self):
        self.driver.quit()

    def test01_loginresult(self):
        self.driver.get('https://apichunmian.qufenqi.com/')
        name=self.driver.find_element(By.CLASS_NAME,'user-name').text
        self.assertEqual("王宽",name,"登录不成功")


    def test02_hosue_lists_page(self):
        self.driver.get('https://apichunmian.qufenqi.com/house/lists')
        name=self.driver.find_element(By.CLASS_NAME,'add-house').text
        self.assertEqual("新增房源",name,"全部房源页面有误")