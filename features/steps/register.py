from behave import *

from features.pages.register_page import RegisterPage


@given(u'I navigate to Register Page')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.open_create_account()
    context.register_page.clickOn_create_account()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for i in context.table:
        context.register_page.enter_details(i["name"], i["number"], i["password"])


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page.continue_to_createAccount()


@then(u'Account should get created')
def step_impl(context):
    assert context.register_page.verifying_accountCreation("Sign Out")


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.register_page.enter_details(" ", " ", " ")


@then(u'Error warning message should be displayed')
def step_impl(context):
    assert context.register_page.verifying_NameError("Enter your name")
    assert context.register_page.verifying_PhoneError("Enter your mobile number")
