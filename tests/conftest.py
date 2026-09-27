import pytest
from selenium import webdriver

from config import Config


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def open_app(driver):
    driver.get(Config.BASE_URL)

    return driver