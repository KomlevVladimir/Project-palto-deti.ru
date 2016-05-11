from pages.page import Page
from selenium.webdriver.common.by import By



class ThirdPage(Page):

    @property
    def Item25(self):
        return self.driver.find_element_by_class_name("post-237")

    @property
    def first_page_link(self):
        return self.driver.find_element_by_link_text("1")

    @property
    def second_page_link(self):
        return self.driver.find_element_by_link_text("2")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CLASS_NAME, "post-237"))