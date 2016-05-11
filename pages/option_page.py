# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class OptionPage(Page):

    @property
    def choose_size(self):
        self.wait.until(presence_of_element_located((By.ID, "pa_%d1%80%d0%b0%d0%b7%d0%bc%d0%b5%d1%80")))
        return Select(self.driver.find_element_by_id("pa_%d1%80%d0%b0%d0%b7%d0%bc%d0%b5%d1%80"))

    @property
    def add_to_cart_button(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "single_add_to_cart_button")))
        return self.driver.find_element_by_class_name("single_add_to_cart_button")

    @property
    def zoom_link(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "woocommerce-main-image")))
        return self.driver.find_element_by_class_name("woocommerce-main-image")

    @property
    def is_zoomed(self):
        return self.is_element_visible((By.ID, "fullResImage"))

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CLASS_NAME, "product_title"))

