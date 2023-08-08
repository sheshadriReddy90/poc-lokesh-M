from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class verifying_login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_xpath = "//span[text()='Account & Lists']/span[@class='nav-icon nav-arrow']"
    check_Sign_out_xpath = "//span[.='Sign Out']"

    def verifying_login(self):
        self.Action_chain("account_xpath", self.account_xpath)

    def check_sign_out(self):
        assert self.display("self.check_Sign_out_xpath", self.check_Sign_out_xpath)
