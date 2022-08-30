import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements





class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # поле поиска
    search = WebElement(id='search-field')

    # кнопка поиска
    search_run_button = WebElement(xpath='//*[@id="searchform"]/div[1]/button/span[1]')

    # Название продуктов  в списке
    products_titles = ManyWebElements(xpath='//a[contains(@class, "product-title") and @title!=""]')



#Локторы элементов главной страницы
#Локаторы элементов  header:
    header_bell = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[1]/span')
    header_bell_second = WebElement(xpath='//div[contains(text(), "У вас пока нет сообщений!")]')
    header_access = WebElement(xpath='//*[contains (text(), "Полный доступ к Лабиринту")]')

    header_my_lab = WebElement(xpath='//*[contains (@class,"") and @style="white-space: normal;"]')

    header_postponed = WebElement(xpath='//span[contains(text(),"Отложено")]')

    header_basket = WebElement(xpath='//a[contains(@class,"b-header-b-personal-e-link") and @href="/cart/"]')

    header_discount = WebElement(xpath='//span[contains (text(), "Книжные")]')


    header_books = WebElement(xpath='//a[contains(@class,"b-header-b-menu-e-text") and @href="/books/"]')
    header_main2022 = WebElement(xpath='//a[contains(@class,"b-header-b-menu-e-text") and @href="/best/"]')
    header_school = WebElement(xpath='//a[contains(@class,"b-header-b-menu-e-text") and @href="/school/"]')
    header_games = WebElement(xpath='//a[contains(@class,"b-header-b-menu-e-text") and @href="/games/"]')
    header_office = WebElement(xpath='//a[contains(@class,"b-header-b-menu-e-text") and @href="/office/"]')
    header_more = WebElement(xpath='//span[@class="b-header-b-menu-e-link top-link-main have-dropdown-touchlink"]')
    header_club = WebElement(xpath='//a[contains(@class,"b-header-b-menu-e-text") and @href="/club/"]')
    header_region_locator = WebElement(css_selector=".region-location-icon-txt")
    header_deliver = WebElement(xpath='//a[contains (text(), "доставим завтра")]')

    header_logo = WebElement(css_selector='.b-header-b-logo-e-logo')

    header_shipping_payment = WebElement(xpath='//a[contains (text(), "Доставка и оплата")]')

    header_agreement = WebElement(xpath='//a[contains(@class, "b-header") and @href="/agreement/"]')

    header_certificates = WebElement(xpath='//a[contains(@href, "/top/certificates/") and @class="b-header-b-sec-menu-e-link"]')
    header_rating = WebElement(xpath='//a[contains(text(),"Рейтинги")]')
    header_novelty = WebElement(xpath='//a[contains(@class, "b-header-b-sec-menu-e-link") and @href="/novelty/"]')
    header_sale = WebElement(xpath='//a[@href="/sale/"]')
    header_phone_number = WebElement(xpath='//a[@class="b-header-b-sec-menu-e-link geotarget-block-phone geotarget-block-phone-1 dropdown-link have-dropdown-touchlink no-select pointer"]')
    header_contact = WebElement(xpath='//a[contains(@href,"/contact/") and @class="b-header-b-sec-menu-e-link"]')
    header_support = WebElement(xpath='//a[contains(@href,"/support/") and @class="b-header-b-sec-menu-e-link"]')
    header_pickup_points = WebElement(xpath='//a[contains(@href,"/maps/") and @class="b-header-b-sec-menu-e-link"]')
    header_network = WebElement(xpath='//em[contains(text(),"в соцсетях")]')
#  локаторы body
    body_previous_slide = WebElement(xpath='//a[@aria-label="Previous slide"]')
    body_next_slide = WebElement(xpath='//a[@aria-label="Next slide"]')

    body_best_sale_day = WebElement(xpath='//a[contains(text(),"Лучшая покупка дня")]')
    body_what_read = WebElement(xpath='//a[contains(text(),"Что почитать: выбор редакции")]')
    body_stock = WebElement(xpath='// *[ @ id = "right-inner"] / div[3] / div[1] / a')
    body_for_school = WebElement(xpath='//a[@href="/genres/3000/"]')
    body_choose_today = WebElement(xpath='//a[contains(text(),"Читатели выбирают сегодня")]')
    body_books_developments = WebElement(xpath='// *[ @ id = "bottom"] / div[6] / div[1] / a')
    body_books_children = WebElement(xpath='//a[contains(@class,"block-link-title") and @href="/child-now/"]')
    body_for_children = WebElement(xpath='//*[@id="bottom"]/div[10]/div[1]/a')
    body_leaders = WebElement(xpath='//*[@id="bottom"]/div[13]/div[1]/a')
    body_novelty = WebElement(xpath='//*[@id="bottom"]/div[15]/div[1]/a')
    body_review = WebElement(xpath='//*[@id="bottom"]/div[17]/div[1]/a')
    body_watched = WebElement(xpath='//*[@id="body-top"]/div[5]/div[1]/div[2]/div[1]/a')
    body_butoon_search = WebElement(xpath='//*[@id="body-top"]/div[5]/div[1]/div[2]/a')
    body_more_sales = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div/div[1]/div[2]/a')

    policy_agree = WebElement(xpath='//*[@class="cookie-policy__button js-cookie-policy-agree"]')


