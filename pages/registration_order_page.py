from pages.page import Page
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By

class RegistrationOrderPage(Page):

    @property
    def first_name_field(self):
        self.wait.until(presence_of_element_located((By.NAME, "billing_first_name")))
        return self.driver.find_element_by_name("billing_first_name")

    @property
    def last_name_field(self):
        return self.driver.find_element_by_name("billing_last_name")

    @property
    def email_field(self):
        return self.driver.find_element_by_name("billing_email")

    @property
    def phone_field(self):
        return self.driver.find_element_by_name("billing_phone")

    @property
    def address_field(self):
        return self.driver.find_element_by_name("billing_address_1")

    @property
    def city_field(self):
        return self.driver.find_element_by_name("billing_city")

    @property
    def state_field(self):
        return self.driver.find_element_by_name("billing_state")

    @property
    def postcode_field(self):
        return self.driver.find_element_by_name("billing_postcode")

    @property
    def confirm_order_button(self):
        self.wait.until(presence_of_element_located((By.NAME, "woocommerce_checkout_place_order")))
        return self.driver.find_element_by_name("woocommerce_checkout_place_order")

    @property
    def cash_checkbox(self):
        self.wait.until(presence_of_element_located((By.ID, "payment_method_cod")))
        return self.driver.find_element_by_id("payment_method_cod")




