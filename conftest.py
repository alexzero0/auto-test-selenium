import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.language
    if 'language' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("language", [option_value])


@pytest.fixture
def browser():
    s = Service(r"F:\chromedriver_win32\chromedriver.exe")
    browser = webdriver.Chrome(service=s)#service=s
    yield browser
    browser.quit()
