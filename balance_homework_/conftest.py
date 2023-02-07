import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    yield driver
    driver.quit()
