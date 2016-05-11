# -*- coding: utf-8 -*-
from pages.page import Page
from selenium.webdriver.common.by import By

class TakenOrderPage(Page):

    @property
    def is_this_page(self):
       return self.is_element_visible((By.CSS_SELECTOR, "h1.entry-title"))