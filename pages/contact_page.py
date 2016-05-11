# -*- coding: utf-8 -*-
from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class ContactPage(Page):

    @property
    def is_this_page(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "entry-title")))
        if self.driver.find_element_by_class_name("entry-title").text == u"Контакты":
            return True
        else:
            return False