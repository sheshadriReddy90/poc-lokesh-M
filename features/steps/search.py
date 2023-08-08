from behave import *
from features.pages.home_page import HomePage


@given(u'I got navigated to Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_homepage_display()


@when(u'I enter valid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_into_search_box(product)


@when(u'I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_searchButton()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    context.search_page.verify_search("Apple iPhone 14 Pro Max (256 GB) - Gold")


@when(u'I enter invalid product say "{product}" into the Search box field')
def step_impl(context, product):
    context.home_page.enter_into_search_box(product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    context.search_page.verify_search_for_invalidProduct()


@when(u'I dont enter anything into Search box field')
def step_impl(context):
    context.home_page.enter_into_search_box("")


@then(u'Proper message should be displayed in Search results on search page')
def step_impl(context):
    assert context.search_page.verify_search_for_blankProduct("")
