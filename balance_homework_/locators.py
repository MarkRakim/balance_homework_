from selenium.webdriver.common.by import By

LOCATOR_GOOGLE_SEARCH_FIELD = (By.XPATH, "//input[@type='text' and @title='Search']")
LOCATOR_GOOGLE_SEARCH_BUTTON = (By.XPATH, "(//input[@type='submit' and @aria-label='Google Search'])[1]")
LOCATOR_GOOGLE_SEARCH_RESULTS = (By.XPATH,
                                 "//div[@data-header-feature='0']/div/a[@data-ved][preceding::div[@id='result-stats']][following::span[text()='Related searches']]")
