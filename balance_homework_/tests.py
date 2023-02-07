from pages.google_page import SearchHelper


def check_word(search_word, results):
    for word in results:
        if search_word in word:
            return True
    return False


def test_search_svyaznoy(browser):
    """
    Если вводим в поисковую строку гугл - apple macbook и нажимаем на кнопку поиска,
    То ожидаем, что:
        - в результатах поиска присутствует svyaznoy.ru
        - в результатах поиска svyaznoy.ru входит в топ 10
    """
    search_msg = "svyaznoy.ru"
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word("apple macbook")
    google_main_page.click_on_the_search_button()
    results = google_main_page.get_search_results()
    assert check_word(search_msg, results), f"{search_msg} не было найдено в результатах поиска"
    assert check_word(search_msg, results[:10]), f"{search_msg} не было найдено в первых 10 результатах поиска"
