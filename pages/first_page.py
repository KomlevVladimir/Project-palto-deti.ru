from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class FirstPage(Page):

    @property
    def Item1(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-477")))
        return self.driver.find_element_by_class_name("post-477")

    @property
    def Item2(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-305")))
        return self.driver.find_element_by_class_name("post-305")

    @property
    def Item3(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-324")))
        return self.driver.find_element_by_class_name("post-324")

    @property
    def Item4(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-378")))
        return self.driver.find_element_by_class_name("post-378")

    @property
    def Item5(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-438")))
        return self.driver.find_element_by_class_name("post-438")

    @property
    def Item6(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-464")))
        return self.driver.find_element_by_class_name("post-464")

    @property
    def Item7(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-389")))
        return self.driver.find_element_by_class_name("post-389")

    @property
    def Item8(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-532")))
        return self.driver.find_element_by_class_name("post-532")

    @property
    def Item9(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-131")))
        return self.driver.find_element_by_class_name("post-131")

    @property
    def Item10(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-370")))
        return self.driver.find_element_by_class_name("post-370")

    @property
    def Item11(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-329")))
        return self.driver.find_element_by_class_name("post-329")

    @property
    def Item12(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-509")))
        return self.driver.find_element_by_class_name("post-509")

    @property
    def second_page_link(self):
        self.wait.until(presence_of_element_located((By.LINK_TEXT, "2")))
        return self.driver.find_element_by_link_text("2")

    @property
    def third_page_link(self):
        self.wait.until(presence_of_element_located((By.LINK_TEXT, "3")))
        return self.driver.find_element_by_link_text("3")

    @property
    def item_link(self):
        self.wait.until(presence_of_element_located((By.CLASS_NAME, "post-477")))
        return self.driver.find_element_by_class_name("post-477")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CLASS_NAME, "post-477"))