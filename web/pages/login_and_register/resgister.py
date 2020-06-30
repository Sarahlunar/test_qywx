from time import sleep

from selenium.webdriver.common.by import By

from web.pages.base import Base


class Register(Base):
    def register(self):
        self.find(By.CSS_SELECTOR, "#corp_name").send_keys("sarah001")
        self.find(By.CSS_SELECTOR, ".js_corp_industry_text").click()
        self.find(By.CSS_SELECTOR, '#corp_industry > div > table > tbody > tr > td.register_industry_wrap.register_industry_maintype_wrap > div:nth-child(1) > a').click()
        # self.find(By.XPATH, '//*[contains(@data-name, "IT")]').click()
        # self.find(By.XPATH, '//*[contains(@data-name, "互联网和相关服务")]').click()
        self.find(By.CSS_SELECTOR, '#corp_industry > div > table > tbody > tr > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a').click()
        self.find(By.CSS_SELECTOR, '#corp_scale_btn>a').click()
        self.find(By.XPATH, '//*[@id="corp_scale_btn"]/div/ul/li[2]').click()
        self.find(By.CSS_SELECTOR, '#manager_name').send_keys("sarah")
        self.find(By.CSS_SELECTOR, '#register_tel').send_keys("13920649905")
        self.find(By.CSS_SELECTOR, '#get_vcode').click()
        self.find(By.CSS_SELECTOR, '#vcode').send_keys("123456")
        self.find(By.CSS_SELECTOR, '#iagree').click()
        self.find(By.CSS_SELECTOR, '#submit_btn').click()
        sleep(3)
        self._driver.quit()




