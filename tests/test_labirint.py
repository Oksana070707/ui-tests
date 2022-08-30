#!/usr/bin/python3
# -*- encoding=utf8 -*-
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#   python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
# (python3 -m pytest -v --driver chrome --driver-path C:\chromedriver\chromedriver.exe)
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#  Обновить pip: python -m pip install --upgrade pip




#  pytest -v --driver chrome --driver-path C:\chromedriver\chromedriver.exe
#import time

from pages.labirint import MainPage


def test_check_main_search_1(web_browser):
    """ Make sure main search works fine 1. """

    page = MainPage(web_browser)

    page.search = 'Карлсон'

    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() > 0


#поиск по спецсимволам

def test_check_main_search_2(web_browser):
    """ Make sure main search works fine 2. """

    page = MainPage(web_browser)
    page.search = '***'
    page.search_run_button.click()


    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() == 0


# поиск по цифрам
def test_check_main_search_3(web_browser):
    """ Make sure main search works fine 3. """

    page = MainPage(web_browser)
    #time.sleep(3)

    page.search = '000'
    #time.sleep(3)
    page.search_run_button.click()
    #time.sleep(3)

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() > 0


#поиск по пустому полю
def test_check_main_search_4(web_browser):
    """ Make sure main search works fine 4. """

    page = MainPage(web_browser)
    page.search = ''
    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() > 0

#поиск на латинице
def test_check_main_search_5(web_browser):
    """ Make sure main search works fine 5. """

    page = MainPage(web_browser)
    page.search = 'dog'
    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() > 0

#поиск по отрицательным числам
def test_check_main_search_6(web_browser):
    """ Make sure main search works fine 6. """

    page = MainPage(web_browser)
    page.search = '-456'
    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() > 0


#поиск по нескольким словам
def test_check_main_search_7(web_browser):
    """ Make sure main search works fine 7. """

    page = MainPage(web_browser)
    page.search = 'кот и пёс'
    page.search_run_button.click()

    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() > 0

#поиск по большому количеству символов, не имеющих смысла
def test_check_main_search_8(web_browser):
    """ Make sure main search works fine 8. """

    page = MainPage(web_browser)
    page.search = 'фыоаывоаивыломивалобмоисичбт бтч итбсчимюоВЫИмбтЯИЧбт иапофорпоркфправлорорморвялоарорволрауокшроасичтьтис675'
    page.search_run_button.click()


    # Проверяем  наличие продуктов на странице:
    assert page.products_titles.count() == 0




# Проверка пунктов меню header:

def test_header_bell_9(web_browser):
    """"Header bell 9. """
    page = MainPage(web_browser)
    page.header_bell.click()

    page.header_access.is_visible()

def test_header_my_lab_10(web_browser):
    """"Header my lab 10. """
    page = MainPage(web_browser)
    page.header_my_lab.click()

    page.header_access.is_visible()

def test_header_postponed_11(web_browser):
    """"Header Postponed 11. """

    page = MainPage(web_browser)
    page.header_postponed.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_header_basket_12(web_browser):
    """" Header Basket 12. """

    page = MainPage(web_browser)
    page.header_basket.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'

def test_header_discount_13(web_browser):
    """" Header discount 13. """

    page = MainPage(web_browser)
    page.header_discount.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'

def test_header_books_14(web_browser):
    """" Header books 14. """

    page = MainPage(web_browser)
    page.header_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/books/'

def test_header_main2022_15(web_browser):
    """'Main2022 15. """

    page = MainPage(web_browser)
    page.header_main2022.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/'

def test_header_school_16(web_browser):
    """header school 16. """

    page = MainPage(web_browser)
    page.header_school.click()

    assert page.get_current_url() == 'https://www.labirint.ru/school/'


def test_header_games_17(web_browser):
    """header games 17. """

    page = MainPage(web_browser)
    page.header_games.click()

    assert page.get_current_url() == 'https://www.labirint.ru/games/'

def test_header_office_18(web_browser):
    """header office 18. """

    page = MainPage(web_browser)
    page.header_office.click()

    assert page.get_current_url() == 'https://www.labirint.ru/office/'

def test_header_more_19(web_browser):
    """header more 19. """

    page = MainPage(web_browser)
    page.header_more.click()

    page.header_more.is_clickable()

def test_header_club_20(web_browser):
    """header club 20. """

    page = MainPage(web_browser)
    page.header_club.click()

    assert page.get_current_url() == 'https://www.labirint.ru/club/'

def test_header_region_locator_21(web_browser):
    """header region 21. """

    page = MainPage(web_browser)
    page.header_region_locator.click()

    page.header_region_locator.is_clickable()

def test_header_deliver_22(web_browser):
    """header deliver 22. """

    page = MainPage(web_browser)
    page.header_deliver.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'

def test_header_logo_23(web_browser):
    """header logo 23. """

    page = MainPage(web_browser)
    page.header_logo.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'

def test_header_shipping_payment_24(web_browser):
    """header shipping payment 24. """

    page = MainPage(web_browser)
    page.header_shipping_payment.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'

def test_header_agreement_25(web_browser):
    """header agreement 25. """

    page = MainPage(web_browser)
    page.header_agreement.click()

    assert page.get_current_url() == 'https://www.labirint.ru/agreement/'

def test_header_certificates_26(web_browser):
    """header certificates 26. """

    page = MainPage(web_browser)
    page.header_certificates.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'

def test_header_rating_27(web_browser):
    """header rating 27. """

    page = MainPage(web_browser)
    page.header_rating.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'

def test_header_novelty_28(web_browser):
    """header novelty 28. """

    page = MainPage(web_browser)
    page.header_novelty.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'

def test_header_sale_29(web_browser):
    """header sale 29. """

    page = MainPage(web_browser)
    page.header_sale.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'

def test_header_phone_number_30(web_browser):
    """header phone 30. """

    page = MainPage(web_browser)
    page.header_phone_number.click()

    page.header_phone_number.is_clickable()

def test_header_contact_31(web_browser):
    """header contact 31. """

    page = MainPage(web_browser)
    page.header_contact.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'

def test_header_support_32(web_browser):
    """header support 32. """

    page = MainPage(web_browser)
    page.header_support.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'

def test_header_pickup_points_33(web_browser):
    """header pickup points 33. """

    page = MainPage(web_browser)
    page.header_pickup_points.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


def test_header_network_34(web_browser):
    """header network 34. """

    page = MainPage(web_browser)
    page.header_network.click()

    page.header_network.is_clickable()

def test_body_previous_slide_35(web_browser):
    """body pre_slide 35. """

    page = MainPage(web_browser)
    page.body_previous_slide.click()

    page.body_previous_slide.is_clickable()

def test_body_next_slide_36(web_browser):
    """body next_slide 36. """

    page = MainPage(web_browser)
    page.body_next_slide.click()

    page.body_next_slide.is_clickable()

def test_body_best_sale_day_37(web_browser):
    """body best sale 37. """

    page = MainPage(web_browser)
    page.body_best_sale_day.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/sale/'


def test_body_what_read_38(web_browser):
    """body what read 38. """

    page = MainPage(web_browser)

    page.policy_agree.scroll_to_element()
    page.policy_agree.click()
    page.wait_page_loaded()

    page.body_what_read.scroll_to_element()
    page.body_what_read.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/top/toread/'


def test_body_stock_39(web_browser):
    """body stock 39. """

    page = MainPage(web_browser)
    page.body_stock.scroll_to_element()
    page.body_stock.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/actions/'

def test_body_for_school_40(web_browser):
    """body for school 40. """

    page = MainPage(web_browser)
    page.body_for_school.scroll_to_element()
    page.body_for_school.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/genres/3000/'


def test_body_choose_today_41(web_browser):
    """body choose today 41. """

    page = MainPage(web_browser)
    page.body_choose_today.scroll_to_element()
    page.body_choose_today.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/best/'


def test_body_books_developments_42(web_browser):
    """body developments 42. """

    page = MainPage(web_browser)
    page.body_books_developments.scroll_to_element()
    page.body_books_developments.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/now/'

def test_body_books_children_43(web_browser):
    """body books children 43. """

    page = MainPage(web_browser)
    page.body_books_children.scroll_to_element()
    page.body_books_children.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/child-now/'

def test_body_for_children_44(web_browser):
    """body for children 44. """

    page = MainPage(web_browser)
    page.body_for_children.scroll_to_element()
    page.body_for_children.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/best/kids/'

def test_body_leaders_45(web_browser):
    """body leaders 45. """

    page = MainPage(web_browser)
    page.body_leaders.scroll_to_element()
    page.body_leaders.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?period=2&id_genre=1852'


def test_body_novelty_46(web_browser):
    """body novelty 46. """

    page = MainPage(web_browser)
    page.body_novelty.scroll_to_element()
    page.body_novelty.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'

def test_body_review_47(web_browser):
    """body review 47. """

    page = MainPage(web_browser)
    page.body_review.scroll_to_element()
    page.body_review.click()
    page.wait_page_loaded()

    assert page.get_current_url() =='https://www.labirint.ru/news/books/'


def test_body_watched_48(web_browser):
    """body watched 48. """

    page = MainPage(web_browser)
    page.body_watched.scroll_to_element()
    page.body_watched.click()
    page.wait_page_loaded()

    assert page.get_current_url() =='https://www.labirint.ru/cabinet/?vybor=visited'


def test_body_butoon_search_49(web_browser):
    """body search 49. """

    page = MainPage(web_browser)
    page.body_butoon_search.scroll_to_element()
    page.body_butoon_search.click()
    page.wait_page_loaded()

    assert page.get_current_url() =='https://www.labirint.ru/now/'

def test_body_more_sales_50(web_browser):
    """body more sales 50. """

    page = MainPage(web_browser)
    page.body_more_sales.scroll_to_element()
    page.body_more_sales.click()
    page.wait_page_loaded()

    assert page.get_current_url() =='https://www.labirint.ru/best/sale/'






















































