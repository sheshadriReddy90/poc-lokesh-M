from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@given(u'I navigated to Login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.amazon.in/ref=ap_frn_logo")
    context.driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_ya_signin']").click()


@when(u'I enter valid email address and valid password as into the fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(8105000676)
    context.driver.find_element(By.ID, 'continue').click()
    context.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Loki@1234")


@when(u'I click on Login button')
def step_impl(context):
    context.driver.find_element(By.ID, "auth-signin-button").click()


@then(u'I should get logged in')
def step_impl(context):
    action = ActionChains(context.driver)
    action.move_to_element(context.driver.find_element(By.XPATH,
                                                       "//span[text()='Account & Lists']/span[@class='nav-icon nav-arrow']")).perform()
    assert context.driver.find_element(By.XPATH, "//span[.='Sign Out']").is_displayed()


@then(u'I should get a proper warning message')
def step_impl(context):
    a = "Incorrect phone number"
    assert context.driver.find_element(By.XPATH, "//h4[.='Incorrect phone number']").text.__eq__(a)


@then(u'I should get a proper warning message on password page')
def step_impl(context):
    a = "Your password is incorrect"
    assert context.driver.find_element(By.XPATH, "//span[contains(.,'Your password is incorrect')]").text.__eq__(a)


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(8105000676)
    context.driver.find_element(By.ID, 'continue').click()
    context.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Loki@1214")


@when(u'I dont enter anything into email field')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("")
    context.driver.find_element(By.ID, 'continue').click()


@then(u'I should get a proper warning message for email failure')
def step_impl(context):
    a = "Enter your email or mobile phone number"
    assert context.driver.find_element(By.XPATH, "//div[contains(text(),'Enter your email or mobile phone number')]").text.__eq__(a)


@when(u'I enter invalid email')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(8105000677)
    context.driver.find_element(By.ID, 'continue').click()
