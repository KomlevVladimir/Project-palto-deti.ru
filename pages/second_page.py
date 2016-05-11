from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located



class SecondPage(Page):

    @property
    def Item13(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-515")))
        return self.driver.find_element_by_class_name("post-515")

    @property
    def Item14(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-524")))
        return self.driver.find_element_by_class_name("post-524")

    @property
    def Item15(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-53")))
        return self.driver.find_element_by_class_name("post-53")

    @property
    def Item16(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-146")))
        return self.driver.find_element_by_class_name("post-146")

    @property
    def Item17(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-157")))
        return self.driver.find_element_by_class_name("post-157")

    @property
    def Item18(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-164")))
        return self.driver.find_element_by_class_name("post-164")

    @property
    def Item19(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-138")))
        return self.driver.find_element_by_class_name("post-138")

    @property
    def Item20(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-240")))
        return self.driver.find_element_by_class_name("post-240")

    @property
    def Item21(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-229")))
        return self.driver.find_element_by_class_name("post-229")

    @property
    def Item22(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-224")))
        return self.driver.find_element_by_class_name("post-224")

    @property
    def Item23(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-194")))
        return self.driver.find_element_by_class_name("post-194")

    @property
    def Item24(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-226")))
        return self.driver.find_element_by_class_name("post-226")

    @property
    def first_page_link(self):
        self.wait.until(presence_of_element_located((By.LINK_TEXT, "1")))
        return self.driver.find_element_by_link_text("1")

    @property
    def third_page_link(self):
        self.wait.until(presence_of_element_located((By.LINK_TEXT, "3")))
        return self.driver.find_element_by_link_text("3")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CLASS_NAME, "post-524"))