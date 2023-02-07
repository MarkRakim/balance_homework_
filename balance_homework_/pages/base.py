from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://google.com/"

    def wait(self):
        return WebDriverWait(self.driver, timeout=DEFAULT_TIMEOUT)

    def find_element(self, locator):
        return self.wait().until(EC.presence_of_element_located(locator),
                                 message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return self.wait().until(EC.presence_of_all_elements_located(locator),
                                 message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
