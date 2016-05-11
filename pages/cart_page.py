# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from pages.page import Page
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class CartPage(Page):

    @property
    def remove_from_cart_button(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "remove")))
        return self.driver.find_element_by_class_name("remove")

    @property
    def return_to_shop_button(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "wc-backward")))
        return self.driver.find_element_by_class_name("wc-backward")

    @property
    def quantity_field(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "input-text")))
        return self.driver.find_element_by_class_name("input-text")

    @property
    def cancel_remove_button(self):
        self.wait.until(presence_of_element_located((By.LINK_TEXT, u"Отменить?")))
        return self.driver.find_element_by_link_text(u"Отменить?")

    @property
    def update_cart_button(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "button")))
        return self.driver.find_element_by_class_name("button")

    @property
    def go_to_registration_button(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "checkout-button")))
        return self.driver.find_element_by_class_name("checkout-button")

    @property
    def is_not_empty_cart(self):
        return self.is_element_visible((By.CLASS_NAME, "cart_item"))

    @property
    def is_empty_cart(self):
        return self.is_element_visible((By.CLASS_NAME, "cart-empty"))

    @property
    def condition_is_satisfied(self):
        quantity = int(self.driver.find_element_by_class_name("input-text").get_attribute("value"))
        product_price = float(((self.driver.find_element_by_css_selector("td.product-price > span.amount").text).replace(',', '.')[:-7]))
        total_price = float(((self.driver.find_element_by_css_selector("td.product-subtotal > span.amount").text).replace(',', '.')[:-7]))
        if total_price == product_price * quantity:
            return True
        else:
            return False