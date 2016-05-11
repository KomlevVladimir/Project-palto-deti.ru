# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pages.cart_page import CartPage
from pages.first_page import FirstPage
from pages.option_page import OptionPage
from pages.second_page import SecondPage
from pages.third_page import ThirdPage
from pages.registration_order_page import RegistrationOrderPage
from pages.taken_order_page import TakenOrderPage
from pages.search_result_page import SearchResultPage
from pages.contact_page import ContactPage
from pages.pay_shipping_page import PayShippingPage
from pages.about_shop_page import AboutShopPage
from pages.for_women_page import ForWomenPage
from pages.for_men_page import ForMenPage


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 10)
        self.first_page = FirstPage(driver, base_url)
        self.second_page = SecondPage(driver, base_url)
        self.third_page = ThirdPage(driver, base_url)
        self.option_page = OptionPage(driver, base_url)
        self.cart_page = CartPage(driver, base_url)
        self.registration_order_page = RegistrationOrderPage(driver, base_url)
        self.taken_order_page = TakenOrderPage(driver, base_url)
        self.search_result_page = SearchResultPage(driver, base_url)
        self.contact_page = ContactPage(driver, base_url)
        self.pay_shipping_page = PayShippingPage(driver, base_url)
        self.about_shop_page = AboutShopPage(driver, base_url)
        self.for_women_page = ForWomenPage(driver, base_url)
        self.for_men_page = ForMenPage(driver, base_url)

    def go_to_main_page(self):
        self.first_page.main_page_link.click()

    def go_to_home_page(self):
        self.first_page.home_page_link.click()

    def go_to_shop_from_cart(self):
        self.cart_page.return_to_shop_button.click()

    def go_to_second_page(self):
        self.first_page.second_page_link.click()

    def go_to_third_page(self):
        self.first_page.third_page_link.click()

    def go_to_contact_page(self):
        main_page = self.first_page
        main_page.contact_page_link.click()

    def go_to_pay_shipping_page(self):
        main_page = self.first_page
        main_page.pay_shipping_page_link.click()

    def go_to_about_shop_page(self):
        main_page = self.first_page
        main_page.about_shop_page_link.click()

    def go_to_for_women_page(self):
        main_page = self.first_page
        main_page.for_women_page_link.click()

    def go_to_for_men_page(self):
        main_page = self.first_page
        main_page.for_men_page_link.click()

    def go_to_for_kids_page(self):
        main_page = self.first_page
        main_page.for_kids_page_link.click()

    def choose_item_from_first_page(self, sizes):
        self.first_page.Item1.click()
        self.option_page.choose_size.select_by_value(sizes.size)

    def choose_item_from_second_page(self, sizes):
        self.first_page.second_page_link.click()
        self.second_page.Item15.click()
        self.option_page.choose_size.select_by_value(sizes.size)

    def choose_item_from_third_page(self, sizes):
        self.first_page.third_page_link.click()
        self.third_page.Item25.click()
        self.option_page.choose_size.select_by_value(sizes.size)

    def add_to_cart(self):
        self.option_page.add_to_cart_button.click()

    def go_to_cart(self):
        self.option_page.cart_link.click()

    def remove_from_cart(self):
        self.cart_page.remove_from_cart_button.click()

    def is_added_to_cart(self):
        return self.cart_page.is_not_empty_cart

    def is_not_added_to_cart(self):
        return self.cart_page.is_empty_cart

    def cancel_remove(self):
        self.cart_page.cancel_remove_button.click()

    def edit_cart(self):
        cart_page = self.cart_page
        cart_page.quantity_field.click()
        cart_page.quantity_field.send_keys(Keys.CONTROL, "a")
        cart_page.quantity_field.send_keys("2")

    def update_cart(self):
        self.cart_page.update_cart_button.click()

    def is_edited_cart(self):
        return self.cart_page.condition_is_satisfied

    def go_to_registration(self):
        self.cart_page.go_to_registration_button.click()

    def registration_order(self, orders):
        registration_order_page = self.registration_order_page
        registration_order_page.first_name_field.send_keys(orders.name)
        registration_order_page.last_name_field.send_keys(orders.lastname)
        registration_order_page.email_field.send_keys(orders.email)
        registration_order_page.phone_field.send_keys(orders.phone)
        registration_order_page.address_field.send_keys(orders.adress)
        registration_order_page.city_field.send_keys(orders.city)
        registration_order_page.state_field.send_keys(orders.state)
        registration_order_page.postcode_field.send_keys(orders.postcode)
        registration_order_page.cash_checkbox.click()
        registration_order_page.confirm_order_button.click()

    def is_registrated(self):
        return self.taken_order_page.is_this_page

    def search(self, searchpar):
        main_page = self.first_page
        main_page.search_field.clear()
        main_page.search_field.send_keys(searchpar.param)
        main_page.search_field.send_keys(Keys.RETURN)

    def is_found(self):
        return self.search_result_page.found_result_condition

    def is_not_found(self):
        return self.search_result_page.unfound_result_condition

    def view_item(self):
        self.first_page.item_link.click()

    def item_is_viewed(self):
        return self.option_page.is_this_page

    def get_zoom_image(self):
        self.option_page.zoom_link.click()

    def image_is_zoomed(self):
        return self.option_page.is_zoomed

    def is_in_contact_page(self):
        return self.contact_page.is_this_page

    def is_in_pay_shipping_page(self):
        return self.pay_shipping_page.is_this_page

    def is_in_about_shop_page(self):
        return self.about_shop_page.is_this_page

    def is_in_for_women_page(self):
        return self.for_women_page.is_this_page

    def is_in_for_men_page(self):
        return self.for_men_page.is_this_page

    def is_in_for_kids_page(self):
        return self.first_page.is_this_page