# -*- coding: utf-8 -*-
from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class SearchResultPage(Page):

    @property
    def found_result_condition(self):
        self.wait.until(presence_of_element_located((By.TAG_NAME, "h3")))
        if self.driver.find_element_by_tag_name("h3").text == u"Детские брюки":
            return True
        else:
            return False

    @property
    def unfound_result_condition(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "woocommerce-info")))
        if self.driver.find_element_by_class_name("woocommerce-info").text == u"Товаров, соответствующих вашему запросу, не обнаружено.":
            return True
        else:
            return False