# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By


class Page(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self. wait = WebDriverWait(driver, 10)

    @property
    def main_page_link(self):
        self.wait.until(presence_of_element_located((By.LINK_TEXT, u"Главная")))
        return self.driver.find_element_by_link_text(u"Главная")

    @property
    def home_page_link(self):
        self.wait.until(presence_of_element_located((By.ID, "menu-item-16")))
        return self.driver.find_element_by_id("menu-item-16")

    @property
    def cart_link(self):
        return self.driver.find_element_by_class_name("cart-contents")

    @property
    def contact_page_link(self):
        return self.driver.find_element_by_id("menu-item-50")

    @property
    def pay_shipping_page_link(self):
        return self.driver.find_element_by_id("menu-item-51")

    @property
    def about_shop_page_link(self):
        return self.driver.find_element_by_id("menu-item-52")

    @property
    def for_women_page_link(self):
        return self.driver.find_element_by_id("menu-item-17")

    @property
    def for_men_page_link(self):
        return self.driver.find_element_by_id("menu-item-18")

    @property
    def for_kids_page_link(self):
        return self.driver.find_element_by_id("menu-item-16")

    @property
    def search_field(self):
        return self.driver.find_element_by_class_name("search-field")

    @property
    def search_field(self):
        return self.driver.find_element_by_class_name("search-field")

    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_element_located(locator))
        except WebDriverException:
            return False

