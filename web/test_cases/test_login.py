import shelve
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

class TestDemo:
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
    #获取cookie
    def test_get_cookie(self):
        db = shelve.open('../datas/test_cookie/cookies')
        db['cookie'] = self.driver.get_cookies()

    # 设置cookie
    def test_set_cookie(self):
        db = shelve.open('../datas/test_cookie/cookies')
        cookies = db['cookie']
        db.close()
        # 添加cookie前要先访问页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookie中的expiry如果是小数就会报错, 需要删掉
        for c in cookies:
            if "expiry" in c.keys():
                c.pop("expiry")
            self.driver.add_cookie(c)
        #添加后再访问一次
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
