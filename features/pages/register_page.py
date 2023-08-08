from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    create_account_xpath = "//a[@data-csa-c-content-id='nav_ya_signin']"
    create_account_submit_id = "createAccountSubmit"
    name_id = "ap_customer_name"
    phone_number_id = 'ap_phone_number'
    password_id = "ap_password"
    continue_id = 'continue'
    verify_button_xpath = "//input[@id='auth-verify-button']"
    verifying_accountCreation_xpath = "//span[text()='Account & Lists']/span[@class='nav-icon nav-arrow']"
    sign_out_xpath = "//span[.='Sign Out']"
    verifying_NameError_xpath = "//div[contains(text(),'Enter your name')]"
    verifying_PhoneError_xpath = "//div[@class='a-box-inner a-alert-container']/div[contains(.,'Enter your mobile number')]"

    def open_create_account(self):
        self.click_on_element("create_account_xpath", self.create_account_xpath)

    def clickOn_create_account(self):
        self.click_on_element("create_account_submit_id", self.create_account_submit_id)

    def enter_details(self, name, phone, password):
        self.type_into_element("name_id", self.name_id, name)
        self.type_into_element("phone_number_id", self.phone_number_id, phone)
        self.type_into_element("password_id", self.password_id, password)

    def continue_to_createAccount(self):
        self.click_on_element("continue_id", self.continue_id)
        return RegisterPage(self.driver)

    def verifying_accountCreation(self, a):
        self.Action_chain("verifying_accountCreation_xpath", self.verifying_accountCreation_xpath)
        return self.text_equal("sign_out_xpath", self.sign_out_xpath, a)

    def verifying_NameError(self, a):
        return self.text_equal("verifying_NameError_xpath", self.verifying_NameError_xpath, a)

    def verifying_PhoneError(self, b):
        return self.text_equal("verifying_PhoneError_xpath", self.verifying_PhoneError_xpath, b)
