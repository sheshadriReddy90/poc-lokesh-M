from features.pages.BasePage import BasePage
from features.pages.login_page import LoginPage
from features.pages.search_page import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//a[@data-csa-c-content-id='nav_ya_signin']"
    homepage_display_xpath = "//div[@id='nav-logo']"
    search_box_xpath = "//div[@class='nav-search-field ']/input[@aria-label='Search Amazon.in']"
    search_button_xpath = "//input[@id='nav-search-submit-button']"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)
        return LoginPage(self.driver)

    def check_homepage_display(self):
        return self.display("homepage_display_xpath", self.homepage_display_xpath)

    def enter_into_search_box(self, a):
        self.type_into_element("search_box_xpath", self.search_box_xpath, a)

    def click_on_searchButton(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)
