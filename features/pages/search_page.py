from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_xpath = "//a[.='Apple iPhone 14 Pro Max (256 GB) - Gold']"
    invalid_product_search_xpath = "//div[.='No results for 424424sssssssss.']"
    blank_search_verify_xpath = "//div[@class='nav-search-field ']/input[@aria-label='Search Amazon.in']"

    def verify_search(self, a):
        return self.text_equal("search_xpath", self.search_xpath, a)

    def verify_search_for_invalidProduct(self):
        return self.display("invalid_product_search_xpath", self.invalid_product_search_xpath)

    def verify_search_for_blankProduct(self, a):
        return self.text_equal("blank_search_verify_xpath", self.blank_search_verify_xpath, a)
