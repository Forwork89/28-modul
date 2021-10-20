import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru'

        super().__init__(web_driver, url)

    # поле поиска
    search = webElement(xpath='//*[@id="stickyHeader"]/div[3]/div/form/div[2]/input[1]').click()

    # кнопка поиска
    search_run_button = WebElement(xpath='//*[@id="stickyHeader"]/div[3]/div[1]/form[1]/button[1]')

    # Название продуктов  в списке
    products_titles = ManyWebElements(xpath='//*[@id="layoutPage"]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div'
                                            '/div[1]/div/div[1]/div/div[2]/a/div/span/span')

    # Кнопка сортировки по цене
    sort_products_by_price = WebElement(css_selector='//*[@id="layoutPage"]/div[1]/div[4]/div[2]/div[1]'
                                                     '/aside/div[5]/div[2]/div[1]/input[2]')

    # Цены продукта
    products_prices = ManyWebElements(xpath='//*[@id="layoutPage"]/div[1]/div[4]/div[2]/div[2]/div'
                                            '[4]/div[1]/div/div/div[4]/div[1]/div[1]/span[1]')
    # Переход к карточке
    button_cart = ManyWebElements(xpath='//*[@id="layoutPage"]/div[1]/div[4]/div[2]'
                                        '/div[2]/div[4]/div[1]/div/div/div[4]/a')
    # Кнопка в карзину
    basket_button = ManyWebElements(css_selector='//*[@id="layoutPage"]/div[1]/div[4]/div[2]/div[2]/div[4]/'
                                                 'div[1]/div/div/div[4]/div[1]/div[4]/div/div/div/button')


