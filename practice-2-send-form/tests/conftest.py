import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://lms.threadqa.ru/xpath-practice-hub'
    browser.config.timeout = 10.0
    yield
    browser.quit()

    