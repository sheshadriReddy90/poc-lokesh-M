from features.pages.BasePage import BasePage
from features.pages.main_page import verifying_login


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    phone_number_xpath = "//input[@id='ap_email']"
    continue_to_password_id = 'continue'
    password_xpath = "//input[@id='ap_password']"
    login_button_id = "auth-signin-button"
    password_incorrect_xpath = "//span[contains(.,'Your password is incorrect')]"
    phone_number_incorrect_xpath = "//h4[.='Incorrect phone number']"
    failure_xpath = "//div[contains(text(),'Enter your email or mobile phone number')]"

    def enter_phone(self, phone_number):
        self.type_into_element("phone_number_xpath", self.phone_number_xpath, phone_number)
        self.click_on_element("continue_to_password_id", self.continue_to_password_id)

    def enter_password(self, password_text):
        self.type_into_element("password_xpath", self.password_xpath, password_text)

    def click_on_login(self):
        self.click_on_element("login_button_id", self.login_button_id)
        return verifying_login(self.driver)

    def password_failure(self, a):
        return self.contains("password_incorrect_xpath", self.password_incorrect_xpath, a)

    def phone_number_failure(self, a):
        return self.contains("self.phone_number_incorrect_xpath", self.phone_number_incorrect_xpath, a)

    def failure_blank_phone(self, a):
        return self.contains("failure_xpath", self.failure_xpath, a)
