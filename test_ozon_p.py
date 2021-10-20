import pytest

from pages.ozon_pages import MainPage


def test_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'Валенки'
    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() == 24

    # Проверяем наличие в названии слова iphone
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'валенки' in title.lower(), msg

    # Валенки на английском


def test_invalid_serch(web_browser):
    page = MainPage(web_browser)

    page.search = 'dfktyrb'
    page.search_run_button.click()
    assert page.products_titles.count() == 24
    for title in page.products_titles.get_text():
        msg = 'wrong product in search"{}"'.format(title)
        assert 'валенки' in title.lower(), msg


@pytest.mark.xfail(reason="Фильтр по цене не работает")
def test_sort_by_price(web_browser):
    page = MainPage(web_browser)
    page.search = 'обои'
    page.search_run_button.click()

    # Прокрутка до элемента, чтобы он стал виден пользователю
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Получение цен всех выведенных продуктов
    all_prices = page.products_prices.get_text()

    # Конвертирование всех цен из строк в числа
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices)
    print(all_prices)
    print(sorted(all_prices))

    assert all_prices == sorted(all_prices)


def test_sort_by_female(web_browser):
    page = MainPage(web_browser)
    page.search = 'валенки женские'
    page.search_run_button.click()

    # Прокрутка до элемента, чтобы он стал виден пользователю
    page.sort_products_by_female.scroll_to_element()
    page.sort_products_by_female.click()
    page.wait_page_loaded()

    # Получение цен всех выведенных продуктов
    all_female_prod = page.products_female.get_text()

    # Конвертирование всех цен из строк в числа
    all_female_prod = [float(p.replace(' ', '')) for p in all_female_prod]

    # Make sure products are sorted by price correctly:
    assert all_female_prod == sorted(all_female_prod)
    print(all_female_prod)
    print(sorted(all_female_prod))

    assert all_female_prod == sorted(all_female_prod)


def test_sort_all_categories(web_browser):
    page = MainPage(web_browser)
    page.search = 'валенки женские'
    page.search_run_button.click()

    # Прокрутка до элемента, чтобы он стал виден пользователю
    page.sort_products_by_all_categories.scroll_to_element()
    page.sort_products_by_all_categories.click()
    page.wait_page_loaded()

    # Получение цен всех выведенных продуктов
    all_categories = page.products_all_categories.get_text()

    # Конвертирование всех цен из строк в числа
    all_categories = [float(p.replace(' ', '')) for p in all_categories]

    # Make sure products are sorted by price correctly:
    assert all_categories == sorted(all_categories)
    print(all_categories)
    print(sorted(all_categories))

    assert all_categories == sorted(all_categories)

