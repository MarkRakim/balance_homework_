from pages.base import BasePage
import locators


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(locators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(locators.LOCATOR_GOOGLE_SEARCH_BUTTON).click()

    def get_search_results(self):
        all_list = self.find_elements(locators.LOCATOR_GOOGLE_SEARCH_RESULTS)
        return [x.text for x in all_list]
