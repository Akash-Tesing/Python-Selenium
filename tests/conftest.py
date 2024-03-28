import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()

    driver.implicitly_wait(5)
    #driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://www.nasdaqomxnordic.com/news/companynews")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
