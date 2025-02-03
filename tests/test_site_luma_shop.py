import allure

from pages.cart_page import Cart
from pages.home_page import HomePage
from pages.men_page import ManPage
from pages.product_page import ProductPage

home_page = HomePage()
man_page = ManPage()
product_page = ProductPage()
cart = Cart()


def test_open_shop_home_page():
    with allure.step('Открываем домашнюю страницу магазина'):
        home_page.accept_permission_to_process_data().click()


def test_open_page_for_men():
    with allure.step('Открываем страницу с товарами для мужчин'):
        man_page.open_page()


def test_open_hoodies_and_sweatshirts():
    with allure.step('Открываем раздел "Худи и Свитшоты"'):
        man_page.hoodies_and_sweatshirts().click()


def test_open_card_marco_lightweight_active_hoodie():
    with allure.step('Находим худи с названием "Marco Lightweight Active Hoodie" и открываем карточку товара'):
        product_page.product('marco-lightweight-active-hoodie').click()


def test_select_size():
    with allure.step('Выбираем размер товара'):
        product_page.select_size('M').click()


def test_select_color():
    with allure.step('Выбираем цвет товара'):
        product_page.select_color('Green').click()


def test_product_add_to_cart():
    with allure.step('Добавляем товар в карзину'):
        product_page.add_to_cart().click()


def test_should_be_message_added_cart_product():
    with allure.step('Проверяем вывод сообщения об успешном добавлении товара в карзину'):
        product_page.should_be_message_added_cart_product('Marco Lightweight Active Hoodie')


def test_open_cart():
    with allure.step('Открываем карзину'):
        cart.open_cart().click()


def test_should_have_details_of_product():
    with allure.step('Проверяем, что в карзине находится выбраный товар с выбранными размером и цветом'):
        cart.product_name('Marco Lightweight Active Hoodie')
        cart.product_details('M', 'Green')
