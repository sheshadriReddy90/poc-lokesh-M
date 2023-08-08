from datetime import datetime
from behave import *
from features.pages.home_page import HomePage


@given(u'I navigated to Login page')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.login_page = context.homepage.click_on_my_account()


@when(u'I enter valid phone number as "{number}" and valid password as "{password}" into the fields')
def step_impl(context, number, password):
    context.login_page.enter_phone(number)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.verify_login = context.login_page.click_on_login()


@then(u'I should get logged in')
def step_impl(context):
    context.verify_login.verifying_login()
    context.verify_login.check_sign_out()


@when(u'I enter valid phone number as "{number}" and invalid password as "{password}" into the fields')
def step_impl(context, number, password):
    context.login_page.enter_phone(number)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message on password page')
def step_impl(context):
    assert context.login_page.password_failure("Your password is incorrect")


@then(u'I should get a proper warning message for  failure')
def step_impl(context):
    assert context.login_page.failure_blank_phone("Enter your email or mobile phone number")


@when(u'I enter invalid phone number')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_number = int("8105" + time_stamp + "902111")
    context.login_page.enter_phone(invalid_number)


@then(u'I should get a proper warning message on phone number page')
def step_impl(context):
    assert context.login_page.phone_number_failure("Incorrect phone number")


@when(u'I dont enter anything into phone number field')
def step_impl(context):
    context.login_page.enter_phone("")
